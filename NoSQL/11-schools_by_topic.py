#!/usr/bin/env python3
"""
this is module
"""
def schools_by_topic(mongo_collection, topic):
    """
    this is function
    """
    return mongo_collection.find({"topics": topic})
