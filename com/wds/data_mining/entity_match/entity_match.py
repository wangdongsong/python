# -*- coding: utf-8 -*-
"""
Created on 2017/12/23 8:33

实体匹配

@author: wangdongsong1229@163.com
"""
import pymysql
import sys
from nltk.metrics import *
from soundex import soundex

db = pymysql.connect(host="localhost", db = "rfrg", user = "", passwd = "", port = 3306, charset = "utf8mb4")

cursor = db.cursor()

#get all projects with matching URLS
cursor.execute("insert into book_entity_matches ( "
               "rf_project_name, "
               "rg_project_name) "
               "select rf.project_name, rg.project_name "
               "from book_rf_entities rf "
               "inner join book_rg_entities rg "
               "on rf.url = rg.url ")

#get projects that have matching project names
cursor.execute("insert into book_entity_matches(rf_project_name, rg_project_name) "
               "select rf.project_name, rg.project_name from "
               "book_rf_entities rf "
               "inner join book_rg_entities rg "
               "on rf.project_name = rg.project_name "
               "where rf.projectname not in ( "
               "select bem.rf_project_name "
               "from book_entity_matches bem)")

#计算每个配对的字符串度量指标
#首先选择这些配对，建立一个循环，单独处理每一对
cursor.execute("select bem.rf_project_name, bem.rg_project_name rfe.url, rge.url "
               "from book_entity_matches bem "
               "inner join book_rg_entities rge "
               "on bem.rg_project_name = rge.project_name "
               "inner join book_rf_entities rfe "
               "on bem.rf_project_name = rfe.project_name "
               "order by bem.rf_project_name")
projectPairs = cursor.fetchall()

peopleQuery = "SELECT rf.dev_username, rf.dev_realname \
               FROM rfrg.book_rf_entity_people rf \
               WHERE rf.project_name =  %s \
               AND (rf.dev_username IN ( \
                    SELECT rg.person_name \
                    FROM rfrg.book_rg_entity_people rg \
                    WHERE rg.project_name =  %s) \
                    OR \
                    rf.dev_realname IN ( \
                    SELECT rg.person_name \
                    FROM rfrg.book_rg_entity_people rg \
                    WHERE rg.project_name = %s))"

updateQuery = "UPDATE book_entity_matches \
               SET rf_name_soundex    = %s,\
                   rg_name_soundex    = %s, \
                   url_levenshtein    = %s, \
                   name_levenshtein   = %s, \
                   rf_name_in_rg_name = %s, \
                   rf_name_in_rg_url  = %s, \
                   rf_dev_in_rg_dev   = %s \
               WHERE rf_project_name = %s \
               AND rg_project_name = %s"

for(projectPair) in projectPairs:
    RFname = projectPair[0]
    RGname = projectPair[1]
    RFurl = projectPair[2]
    RGurl = projectPair[3]

    RFnameLC = RFname.lower()
    RGnameLC = RGname.lower()
    RFurlLC = RFurl.lower()
    RGurlLC = RGurl.lower()

    levNames = edit_distance(RFnameLC, RGnameLC)
    levURLs = edit_distance(RFurlLC, RGurlLC)
    soundexRFname = soundex(RFnameLC)
    soundexRGname = soundex(RGnameLC)

    if RFnameLC in RGnameLC:
        rf_in_rg = 1
    else:
        rf_in_rg = 0

    if RFnameLC in RGurl:
        rf_in_rgurl = 1
    else:
        rf_in_rgurl = 0

    cursor.execute(peopleQuery,
                   (RFname, RGname, RGname))
    result = cursor.fetchone()
    if result is not None:
        rfdev_in_rgdev = 1
    else:
        rfdev_in_rgdev = 0

    cursor.execute(updateQuery,
                   (soundexRFname,
                    soundexRGname,
                    levURLs,
                    levNames,
                    rf_in_rg,
                    rf_in_rgurl,
                    rfdev_in_rgdev,
                    RFname,
                    RGname))

db.close()
