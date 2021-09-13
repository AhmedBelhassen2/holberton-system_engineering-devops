#!/usr/bin/python3
""" Python Script """
import json
import requests
from sys import argv

if __name__ == "__main__":
    u_link = "https://jsonplaceholder.typicode.com/users"
    uid = argv[1]

    u_info = requests.get("{}/{}".format(u_link, uid)).json()
    username = u_info['username']
    todo_info = requests.get("{}/{}/todos".format(u_link, uid)).json()
    file = '{}.json'.format(uid)
    data = dict()
    data[str(uid)] = []
    for todo in todo_info:
        data[str(uid)].append(
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
        )

    with open(file, 'w', newline='') as jsonfile:
        json.dump(data, jsonfile)
