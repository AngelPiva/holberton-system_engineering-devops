#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    file_name = "{}.json".format(argv[1])

    response_user = requests.get(url_users).json()
    response_todos = requests.get(url_todos).json()
    username = response_user.get("username")

    dict = {}
    list = []
    for i in response_todos:
        list.append(i)
    dict[argv[1]] = list

    with open(file_name, "w") as f:
        json.dump(dict, f)
