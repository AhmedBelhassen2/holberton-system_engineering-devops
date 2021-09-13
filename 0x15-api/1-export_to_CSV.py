#!/usr/bin/python3
""" Python script that, for a given employee ID, returns information """
import csv
import requests
import sys
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    userId = int(sys.argv[1])
    user = requests.get(url + "/users/{}".format(userId))
    td = requests.get(url + '/todos')
    name = user.json().get('username')
    file = sys.argv[1] + '.csv'
    with open(file, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
        for t in td.json():
            if t.get('userId') == userId:
                writer.writerow([userId, name, str(t.get('completed')),
                                t.get('title')])
