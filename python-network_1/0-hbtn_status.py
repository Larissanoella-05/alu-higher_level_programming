#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status using urllib"""

import urllib.request

url = 'http://0.0.0.0:5050/status'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))

