#!/usr/bin/python3
"""
Module that interacts with the JSONPlaceholder API.

Contains two functions:
- fetch_and_print_posts(): fetches posts and prints their titles.
- fetch_and_save_posts(): fetches posts and saves them into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder API and print their titles.

    Sends a GET request to the API endpoint, checks if the request
    was successful, converts the response to JSON, and prints
    each post's title.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"{post['title']}")


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder API and save them to a CSV file.

    Sends a GET request to the API endpoint, checks if the request
    was successful, converts the response to JSON, filters relevant
    fields (id, title, body), and writes the data to 'posts.csv'.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)
    print("Status Code:", response.status_code)
