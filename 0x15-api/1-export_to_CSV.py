#!/usr/bin/python3
"""
Export employee TODO list to CSV
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(url).json()

    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos = requests.get(url).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                user_id,
                user["username"],
                str(todo["completed"]),
                todo["title"]
            ])
