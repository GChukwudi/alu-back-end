#!/usr/bin/python3
""" Library to gather data from an API """

import requests
import sys

""" Script to  return a given employee ID
together with his/her TODO list progress
"""

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    todo = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    message = f"Employee {employee_name} is done with tasks({task_com}/{total_task_done}):"
    print(message)
    [print(f"\t{task.get('title')}") for task in total_tasks]
