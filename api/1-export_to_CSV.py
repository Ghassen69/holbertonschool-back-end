#!/usr/bin/python3
"""Fetches and writes to-do list for a given employee ID"""

import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    file_name = str(eval(sys.argv[1])) + ".csv"

    with open(file_name, "x") as f:
        for task in todos:
            row = '"' + str(user.get("id")) + '","' + str(
                user.get("username")) + '","' + str(
                    task.get("completed")) + '","' + str(
                        task.get("title")) + '"\n'
            f.write(row)
