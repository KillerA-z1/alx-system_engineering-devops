#!/usr/bin/python3
"""
Export TODO lists for all employees to a single JSON file
"""
import json
import requests


def fetch_all_users():
    url = "https://jsonplaceholder.typicode.com/users"
    return requests.get(url).json()


def fetch_todos_for_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    return requests.get(url).json()


if __name__ == "__main__":
    all_users = fetch_all_users()
    all_tasks = {}

    for user in all_users:
        user_id = str(user["id"])  # Convert to string for JSON key
        username = user["username"]
        todos = fetch_todos_for_user(user_id)

        user_tasks = []
        for todo in todos:
            user_tasks.append(
                {
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
            )

        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
