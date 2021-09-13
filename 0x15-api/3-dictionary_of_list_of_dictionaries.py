#!/usr/bin/python3
""" script to fetch data from an APIs """

import json
import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/users").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    dct2 = {}
    for j in users:
        lt1 = []
        for i in todos:
            if i.get("userId") == j.get("id"):
                dct1 = {}
                dct1["task"] = i.get("title")
                dct1["completed"] = i.get("completed")
                dct1["username"] = j.get("username")
                lt1.append(dct1)
        dct2[j.get("id")] = lt1

    with open("todo_all_employees.json", 'w') as file:
        jsonobject = json.dumps(dct2)
        file.write(jsonobject)
