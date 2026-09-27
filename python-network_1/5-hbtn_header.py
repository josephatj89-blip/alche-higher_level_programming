#!/usr/bin/python3
"""Fetches a URL and displays the X-Request-Id header from the response."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
