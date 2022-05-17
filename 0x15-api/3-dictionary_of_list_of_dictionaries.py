#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    url_users = "https://jsonplaceholder.typicode.com/users"
    file_name = "todo_all_employees.json"

    response_user = requests.get(url_users).json()
    response_todos = requests.get(url_todos).json()

    all_users = {}
    for u in response_user:
        dict = {}
        list = []
        for i in response_todos:
            in_dict = {}
            in_dict["task"] = i.get("title")
            in_dict["completed"] = i.get("completed")
            in_dict["username"] = u.get("username")
            list.append(in_dict)
        all_users[u.get("id")] = list
    with open(file_name, "w") as f:
        json.dump(all_users, f)
