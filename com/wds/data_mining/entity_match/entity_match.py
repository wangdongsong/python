# -*- coding: utf-8 -*-
"""
Created on 2017/12/23 8:33

实体匹配

@author: wangdongsong1229@163.com
"""
import pymysql
import sys
from nltk.metrics import *

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

for(projectPair) in projectPairs:
    RFname = projectPair[0]
    FGname = projectPair[1]
    RFurl = projectPair[2]
    RGurl = projectPair[3]

    RFnameLC = RFname.lower()
    FGnameLC = FGname.lower()
    RFurlLC = RFurl.lower()
    RGurlLC = RGurl.lower()
