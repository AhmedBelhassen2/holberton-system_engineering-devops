#!/usr/bin/python3
"""Python script that, for a given employee ID, returns information """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    emp = int(argv[1])
    users = requests.get(url + "/users/{}".format(emp))
    name = users.json().get('name')
    t = requests.get(url + '/todos')
    comp = 0
    td = 0
    for d in t.json():
        if d.get('userId') == int(emp):
            td += 1
            if d.get('completed'):
                comp += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, comp, td))
    print('\n'.join(["\t " + d.get('title') for d in t.json()
          if d.get('userId') == emp and d.get('completed')]))
