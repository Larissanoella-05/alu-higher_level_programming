#!/usr/bin/python3
"""Module that fetches the status from a given URL using urllib"""

import urllib.request

def fetch_status(url):
    """Fetches and displays the status of a given URL."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))

if __name__ == "__main__":
    fetch_status('https://intranet.hbtn.io/status')
    fetch_status('http://0.0.0.0:5050/status')
