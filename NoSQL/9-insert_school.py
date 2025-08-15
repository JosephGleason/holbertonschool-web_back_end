#!/usr/bin/env python3
"""Module that contains a function to insert a document in a collection."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection (Collection): The pymongo collection object
            where the document will be inserted.
        **kwargs: Arbitrary keyword arguments representing the fields
            and values of the document to insert. For example:
            name="UCSF", address="505 Parnassus Ave".

    Returns:
        ObjectId: The unique _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
