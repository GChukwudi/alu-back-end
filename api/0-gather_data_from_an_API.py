#!/usr/bin/python3
""" Library to gather data from an API """

import requests
from sys import argv

""" Script to  return a given employee ID
together with his/her TODO list progress
"""

if __name__ == "__main__":
    employee_id = argv[1]
    url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}", verify=False).json()
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}", verify=False).json()
    completed_tasks = [task['title'] for task in todo if task.get('completed')]

    print(f"Employee {url.get('name')} is done with tasks({len(completed_tasks)}/{len(todo)}):")
    print("\n".join([f"\t{task}" for task in completed_tasks]))
