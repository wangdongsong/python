# -*- coding: utf-8 -*-
"""
Created on 2017/12/10 22:00

@author: wangdongsong1229@163.com
"""
import pymysql
import getpass

# here are the two tags we want to compare
X = 'Internet'
Y = 'Web'

# database connection params
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

# grab basic counts from the database
numBasketsQuery = "SELECT count(DISTINCT project_id) FROM fc_project_tags"
cursor.execute(numBasketsQuery)
numBaskets = cursor.fetchone()[0]

supportForXYQuery = "SELECT count(*) FROM fc_project_tags WHERE tag_name=%s"
cursor.execute(supportForXYQuery, (X))
supportForX = cursor.fetchone()[0]

cursor.execute(supportForXYQuery, (Y))
supportForY = cursor.fetchone()[0]

pairSupportQuery = "SELECT num_projs FROM fc_project_tag_pairs WHERE tag1 = %s AND tag2 = %s"
cursor.execute(pairSupportQuery, (X, Y))
pairSupport = cursor.fetchone()[0]

# calculate support : support of pair, divided by num baskets
pairSupportAsPct = pairSupport / numBaskets

# calculate confidence of X->Y
supportForXAsPct = supportForX / numBaskets
confidenceXY = pairSupportAsPct / supportForXAsPct

# calculate confidence of Y->X
supportForYAsPct = supportForY / numBaskets
confidenceYX = pairSupportAsPct / supportForYAsPct

# calculate added value X->Y
AVXY = confidenceXY - supportForYAsPct
AVYX = confidenceYX - supportForXAsPct

print("Support for ", X, "U", Y, ":", round(pairSupportAsPct, 4))
print("Conf.", X, "->", Y, ":", round(confidenceXY, 4))
print("Conf.", Y, "->", X, ":", round(confidenceYX, 4))
print("AV", X, "->", Y, ":", round(AVXY, 4))
print("AV", Y, "->", X, ":", round(AVYX, 4))

db.close()
