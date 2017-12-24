# -*- coding: utf-8 -*-
"""
Created on 2017/12/10 9:46

Purpose: Finds frequent itemsets for tags used to describe Freecode projects.

Notes:
1. Uses a MySQL database to store the tags, doubletons, tripletons. Code for
  SQL setup is in attached file.
2. Minimum support for itemsets is set in the MINSUPPORT constant.

@author: wangdongsong1229@163.com
"""

import itertools
import pymysql
import getpass
import logging

MINSUPPORTPCT = 5 #可以是任意常数，默认为5

allSingletonTags = []
allDoubletonTags = set()
doubletonSet = set()

#连接数据库
dbhost = 'localhost'
dbschema = 'dataming'
dbuser = 'wds'
dbpasswd = getpass.getpass()
dbport = 3306
dbcharset = 'utf8mb4'

# Open local database connection
db = pymysql.connect(host=dbhost,
                     db=dbschema,
                     user=dbuser,
                     passwd=dbpasswd,
                     port=dbport,
                     charset=dbcharset,
                     autocommit=True)
cursor = db.cursor()


#计算篮子数量——数据库表中的项目数
queryBaskets = "select count(distinct project_id) from fc_project_tags;"
cursor.execute(queryBaskets)
baskets = cursor.fetchone()[0]

#使用蓝子数和前面设置的最小支持阈值，计算蓝子的最小数量
minsupport = baskets * (MINSUPPORTPCT / 100)
print("Minimum support count:", minsupport, "(", MINSUPPORTPCT, "% of", baskets, ")")

#得到一组符合最小标签阈值的标签
cursor.execute("select distinct tag_name from fc_project_tags group by 1 having count(project_id) >= %s order by tag_name", (minsupport))
singletons = cursor.fetchall()


def findDoubletons():
    logging.info("Frequent doubletons found:")

    doubletonCandidates = list(itertools.combinations(allSingletonTags, 2))

    for (index, candidate) in enumerate(doubletonCandidates):
        tag1 = candidate[0]
        tag2 = candidate[1]
        cursor.execute("select count(fpt1.project_id) "
                        "from fc_project_tags fpt1 "
                        "inner join fc_project_tags fpt2 "
                        "on fpt1.project_id = fpt2.project_id "
                        "where fpt1.tag_name = %s and fpt2.tag_name = %s"
                        , (tag1, tag2))
        count = cursor.fetchone()[0]
        if count > minsupport:
            logging.info(tag1, tag2, "[", count, "]")
            cursor.execute("insert into fc_project_tag_pairs (tag1, tag2, num_projs) values (%s, %s, %s)", (tag1, tag2, count))
            doubletonSet.add(candidate)
            allDoubletonTags.add(tag1)
            allDoubletonTags.add(tag2)


def findTripletons():
    logging.info("Frequent tripletons found:")
    tripletonCandidates = list(itertools.combinations(allDoubletonTags, 3))
    tripletonCandidatesSorted = []
    for tc in tripletonCandidates:
        tripletonCandidatesSorted.append(sorted(tc))

    for (index, candidate) in enumerate(tripletonCandidatesSorted):
        doubletonsInsideTripleton = list(itertools.combinations(candidate, 2))

        tripletonCandidateRejected = 0

        for(index,  doubleton) in enumerate(doubletonsInsideTripleton):
            if doubleton not in doubletonSet:
                tripletonCandidateRejected = 1
                break
        if tripletonCandidateRejected == 0:
            cursor.execute("select count(fpt1.project_id) "
                           "from fc_project_tags fpt1 "
                           "inner join fc_project_tags fpt2 "
                           "on fpt1.project_id = fpt2.project_id "
                           "inner join fc_project_tags fpt3 "
                           "on fpt2.project_id = fpt3.project_id "
                           "where (fpt1.tag_name = %s "
                           "and fpt2.tag_name = %s "
                           "and fpt3.tag_name = %s )",
                           (candidate[0], candidate[1], candidate[2]))
            count = cursor.fetchone()[0]

            if count > minsupport:
                logging.info(candidate[0], ",", candidate[1], ",", candidate[2], "[", count, "]")

                cursor.execute("insert into fc_project_tag_triples"
                               "(tag1, tag2, tag3, num_projs) "
                               "values (%s, %s, %s, %s)",
                               (candidate[0], candidate[1], candidate[2], count))



def generateRules():
    logging.info("Association Rules:")

    cursor.execute("Select tag1, tag2, tag3, num_projs from fc_project_tag_triples")
    triples = cursor.fetchall()
    for(triple) in triples:
        tag1 = triple[0]
        tag2 = triple[1]
        tag3 = triple[2]
        ruleSupport = triple[3]

        calcSCAV(tag1, tag2, tag3, ruleSupport)
        calcSCAV(tag1, tag3, tag2, ruleSupport)
        calcSCAV(tag2, tag3, tag1, ruleSupport)
        logging.info("*")


def calcSCAV(tagA, tagB, tagC, ruleSupport):
    ruleSupportPct = round((ruleSupport / baskets), 2)
    query1 = "select num_projs from fc_project_tag_pairs where (tag1 = %s and tag2= %s) or (tag2 = %s and tag1 = %s)"
    cursor.execute(query1, (tagA, tagB, tagB, tagA))
    pairSupport = cursor.fetchone()[0]
    confidence = round((ruleSupport / pairSupport), 2)

    query2 = "select count(*) from fc_project_tags where tag_name = %s"
    cursor.execute(query2, tagC)

    supportTagC = cursor.fetchone()[0]
    supportTagCPct = supportTagC / baskets
    addedValue = round((confidence - supportTagCPct), 2)

    print(tagA, ", ", tagB, "->", tagC, "[S=", ruleSupportPct, ", C=", confidence, ", AV=", addedValue, "]")





for(singletons) in singletons:
    allSingletonTags.append(singletons[0])

print("allSingletonTags=", allSingletonTags)

#使用频繁的单例创建侯选二元组
findDoubletons()
findTripletons()
generateRules()
db.close()

