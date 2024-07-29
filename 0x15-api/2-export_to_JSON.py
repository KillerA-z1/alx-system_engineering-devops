#!/usr/bin/python3
"""
Export employee TODO list to JSON
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(url).json()

    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos = requests.get(url).json()

    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"]
        })

    json_data = {user_id: tasks}

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)
