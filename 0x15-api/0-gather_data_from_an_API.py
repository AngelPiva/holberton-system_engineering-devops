#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])
    url_users = "https://jsonplaceholder.typicode.com/users"

    response_user = requests.get(url_users).json()
    response_todos = requests.get(url_todos).json()

    name = ""
    for s_name in response_user:
        if s_name.get("name") == argv[1]:
            name = s_name.get("name")

    tasks_completed = []
    for tasks in response_todos:
        if tasks.get("completed") is True:
            tasks_completed.append(tasks.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(tasks_completed), len(response_todos)))
    for items in tasks_completed:
        print("\t {}".format(items))
