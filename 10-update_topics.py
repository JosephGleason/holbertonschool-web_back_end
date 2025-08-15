#!/usr/bin/env python3
"""
Function to update topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the school name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to match.
        topics (list): The new list of topics to set.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
