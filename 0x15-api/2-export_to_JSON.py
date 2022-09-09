#!/usr/bin/python3
"""Python script to export data in the JSON format
"""
import json
import requests
import sys

if __name__ == '__main__':
    """Python script to export data in the JSON format"""
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f'users/{sys.argv[1]}').json()
    # print(user)
    tasks = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    # print(tasks)
    info_tasks = []
    for task in tasks:
        disct = {'task': task.get('title'),
                 'completed': task.get('completed'),
                 'username': user.get('username')}
        info_tasks.append(disct)
    disct = {f'{sys.argv[1]}': info_tasks}
    # print(disct)

    with open(f'{sys.argv[1]}.json', 'w', encoding='UTF8', newline='') as f:
        json.dump(disct, f)
