#!/usr/bin/env python3
"""Provide stats about Nginx logs"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    count = collection.count_documents({})
    print(f"{count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
