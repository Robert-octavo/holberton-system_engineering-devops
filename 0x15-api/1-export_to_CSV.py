#!/usr/bin/python3
"""Python script to export data in the CSV format
"""
import csv
import requests
import sys


if __name__ == '__main__':
    """Python script to export data in the CSV format"""
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    # print(user)
    tasks = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    # print(tasks)
    info_tasks = []
    user_id = str(sys.argv[1])

    for task in tasks:
        info_tasks.append([user_id,
                           user.get('name'),
                           task.get('completed'),
                           task.get('title')])
    with open(user_id + '.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in info_tasks:
            writer.writerow(task)
