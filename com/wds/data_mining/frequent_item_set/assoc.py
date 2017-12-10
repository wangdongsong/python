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
import logging


def findDoubletons():
    logging.info("Frequent doubletons found:")

    doubletonCandidates = list(itertools.combinations(allSingletonTags, 2))

    for (index, candidate) in enumerate(doubletonCandidates):
        tag1 = candidate[0]
        tag2 = candidate[1]
        cursor.execute(("select count(fpt1.project_id) "
                        "from fc_project_tags fpt1 "
                        "inner join fc_project_tags fpt2 "
                        "on fpt1.project_id = fpt2.project_id "
                        "where fpt1.tag_name = %s and fpt2.tag_name = %s"
                        , (tag1, tag2)))
        count = cursor.fetchone()[0]
        if count > minsupport:
            logging.info(tag1, tag2, "[", count, "]")
            cursor.execute("insert into fc_project_tag_pairs (tag1, tag2, num_projs) values (%s, %s, %s)", (tag1, tag2, count))
            doubletonSet.add(candidate)
            allDoubletonTags.add(tag1)
            allDoubletonTags.add(tag2)


def findTripletons():
    print("==========")


def generateRules():
    print("==========")


MINSUPPORTPCT = 5 #可以是任意常数，默认为5

allSingletonTags = []
allDoubletonTags = set()
doubletonSet = set()

#连接数据库
db = pymysql.connect(host="localhost", db="python", user="test", password="test", port=3306, charset="utf8mb4")

cursor = db.cursor()

#计算篮子数量——数据库表中的项目数
queryBaskets = "select count(distinct project_id) from fc_project_tags;"
cursor.execute(queryBaskets)
baskets = cursor.fetchone()[0]

#使用蓝子数和前面设置的最小支持阈值，计算蓝子的最小数量
minsupport = baskets * (MINSUPPORTPCT / 100)
print("Minimum support count:", minsupport, "(", MINSUPPORTPCT, "%of", baskets, ")")

#得到一组符合最小标签阈值的标签
cursor.execute("select distinct tage_name from fc_project_tags group by 1 having count(project_id) >= %s order by tage_name", (minsupport))
singletons = cursor.fetchall()

for(singletons) in singletons:
    allSingletonTags.append(singletons[0])

#使用频繁的单例创建侯选二元组
findDoubletons()
findTripletons()
generateRules()
db.close()

