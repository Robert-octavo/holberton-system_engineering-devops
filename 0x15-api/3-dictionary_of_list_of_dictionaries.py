#!/usr/bin/python3
"""Python script to export data in the JSON format
"""
import json
from urllib import request
import requests
import sys

if __name__ == '__main__':
    """Python script to export data in the JSON format"""
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    users = requests.get(url_users).json()

    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump({user.get("id"): [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user.get('username')
            } for task in requests.get(url_todos,
                                       params={"userId":
                                               user.get('id')}).json()]
            for user in users}, f)
