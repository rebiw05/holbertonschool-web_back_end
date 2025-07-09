#!/usr/bin/env python3
"""
this document show how to lists
"""
def list_all(mongo_collection):
    """
    this is function
    """
    if mongo_collection is None:
        return []
    documents = list(mongo_collection.find())
    return documents
