#coding=utf-8
import pymongo
from urllib import parse

def connect_sql():
    user = parse.quote_plus("yourname")
    pw = parse.quote_plus("yourpw")
    client = pymongo.MongoClient('mongodb://{}:{}@39.100.120.147:27017/'.format(user, pw))

    return client
