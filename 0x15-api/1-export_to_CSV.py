#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    file_name = "{}.csv".format(argv[1])

    response_user = requests.get(url_users).json()
    response_todos = requests.get(url_todos).json()
    username = response_user.get("username")

    with open(file_name, "w") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for i in response_todos:
            title = i.get('title')
            tasks = i.get('completed')
            w.writerow([int(argv[1]), username, tasks, title])
