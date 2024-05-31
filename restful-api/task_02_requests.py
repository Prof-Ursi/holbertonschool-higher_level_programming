#!/usr/bin/env python3
"""
This module defines two functions.
The first one fetches JSON data from a website and print them,
The second one save them in a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetch posts from the API and print their titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from the API and save them to a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        posts_data = [{
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        } for post in posts]

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
