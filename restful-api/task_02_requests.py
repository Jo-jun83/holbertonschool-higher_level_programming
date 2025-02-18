#!/usr/bin/python3
"""
This module provides functionality to fetch and print posts from a RESTful API.
"""

import requests
import csv

base_url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches posts from a specified base URL and prints their titles.
    """
    response = requests.get(base_url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print(response.status_code)


def fetch_and_save_posts():
    """
    Fetches posts from a specified base URL and saves them to a CSV file.
    """
    response = requests.get(base_url)
    if response.status_code == 200:
        posts = response.json()

        data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
