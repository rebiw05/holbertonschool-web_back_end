#!/usr/bin/env python3
"""
this is module
"""
def insert_school(mongo_collection, **kwargs):
    """
    this is function
    """
    return mongo_collection.insert_one(kwargs).inserted_id
