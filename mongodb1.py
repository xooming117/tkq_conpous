#coding=utf-8

from datetime import datetime
import pymongo
from pymongo import MongoClient

# 连接mongodb数据库
client = MongoClient('mongodb://mongodb:27017/')
# 指定数据库名称
db = client.tbk_database
# 获取非系统的集合
db.collection_names(include_system_collections=False)
print (db.collection_names())


def compare_today(day):
    today = datetime.today()
    today = datetime(today.year, today.month, today.day, 0, 0, 0)
    ymd = day.split('.')
    day1 = datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]))
    if today > day1:
        return 1
    else:
        return 0


def get_today_start():
    today = datetime.today()
    today_start = datetime(today.year, today.month, today.day, 1, 0, 0)
    return today_start


def get_goods():
    c = db.goods
    d = get_today_start()
    # return c.find({'updateAt': {"$lt": d}, 'isDelete': False}).batch_size(30).sort("updateAt",1).limit(100)
    return c.find({'updateAt': {"$lt": d}}).batch_size(30).sort("updateAt",1).limit(100)


def update_goods(g):
    print 'update'
    c = db.goods
    g['updateAt'] = datetime.today()
    c.update({'_id': g['_id']}, g)


def delete_goods(g):
    print 'delete'
    c = db.goods
    g['updateAt'] = datetime.today()
    g['isDelete'] = True
    c.update({'_id': g['_id']}, g)


# today = datetime.today()
# today_start1 = datetime(today.year, today.month, today.day, 1, 0, 1)
# today_start2 = datetime(today.year, today.month, today.day, 1, 0, 1)
# print today_start1
# print today_start2
# if today_start1 > today_start2:
#     print '1>2'
# else:
#     print '1<2'

# today = datetime.today()
# print today