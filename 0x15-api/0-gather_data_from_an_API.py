#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f'users/{sys.argv[1]}').json()
    # print(user)
    tasks = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    # print(tasks)
    complete = []
    for task in tasks:
        if task.get('completed'):
            complete.append(task.get('title'))
    # print(f'{len(tasks)}:{len(complete)}')
    # print(complete)
    print(f'Employee {user.get("name")} is done with \
tasks({len(complete)}/{len(tasks)}):')
    [print(f'\t {i}') for i in complete]
