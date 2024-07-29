#!/usr/bin/python3
"""
Script to fetch and display an employee's TODO list progress using a REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetch todos for the employee
    todos_response = requests.get(f"{base_url}/todos")
    todos_data = todos_response.json()

    # Filter todos for the specific employee
    employee_todos = [
        todo for todo in todos_data
        if todo["userId"] == employee_id
    ]

    # Calculate progress
    total_tasks = len(employee_todos)
    completed_tasks = [todo for todo in employee_todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Display progress
    print(f"Employee {employee_name} is done with tasks("
          f"{num_completed_tasks}/{total_tasks}): ")
    # Display completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
