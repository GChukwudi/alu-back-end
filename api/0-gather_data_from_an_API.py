#!/usr/bin/python3
""" Library to gather data from an API """

import requests
from sys import argv

""" Script to return a given employee ID
together with their TODO list progress
"""

if __name__ == "__main__":
    employee_id = argv[1]
    url = ("https://jsonplaceholder.typicode.com/users/{}"
           .format(employee_id))
    todo = ("https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(employee_id))

    user_info = requests.get(url).json()
    todo_info = requests.get(todo).json()
    completed_tasks = [task['title'] for task in todo_info if task['completed']]

    print("Employee {} is done with tasks({}/{}):"
          .format(user_info['name'], len(completed_tasks), len(todo_info)))
    print("\n".join(["\t{}".format(task) for task in completed_tasks]))
