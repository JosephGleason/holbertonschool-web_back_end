#!/usr/bin/env python3
"""
Module for filtering schools by topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of school documents that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of documents (dicts) where the topic is present.
    """
    return list(mongo_collection.find({"topics": topic}))
