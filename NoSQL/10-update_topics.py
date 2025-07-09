#!/usr/bin/env python3
"""
this is module
"""
def update_topics(mongo_collection, name, topics):
    """
    this is function
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
