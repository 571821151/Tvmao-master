#!/usr/bin/python3
#coding=utf-8

from pymongo import MongoClient
client = MongoClient()

db = client.pythondb

class mongop_util():
    def __init__(self):
        '''sssxxx'''
    def add_bjson(self,post):
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id
        if   post_id:
            return True
        else:
            return False



