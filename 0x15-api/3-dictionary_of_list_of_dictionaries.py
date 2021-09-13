#!/usr/bin/python3
""" Python Script """
import json
import requests

if __name__ == "__main__":
    u_link = "https://jsonplaceholder.typicode.com/users"
    file = 'todo_all_employees.json'

    u_info = requests.get("{}/".format(u_link)).json()
    data = dict()
    for user in u_info:
        uid = user['id']
        username = user['username']
        todo_info = requests.get("{}/{}/todos".format(u_link, uid))
        users = todo_info.json()
        data[str(uid)] = list()
        for todo in users:
            data[str(uid)].append(
                {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
            )

    with open(file, 'w', newline='') as jsonfile:
        json.dump(data, jsonfile)
