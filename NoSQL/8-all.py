#!/usr/bin/env python3
"""
Module 8-all
Contains a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (Collection): A PyMongo collection object.

    Returns:
        list: A list of all documents in the collection.
              Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())
