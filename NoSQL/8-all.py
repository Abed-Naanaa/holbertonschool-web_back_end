#!/usr/bin/env python3
""" List all documents in a collection """

def list_all(mongo_collection):
    return list(mongo_collection.find())
