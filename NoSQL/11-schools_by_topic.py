#!/usr/bin/env python3
"""
Module that provides functionality to query a MongoDB collection 
for schools that have a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
