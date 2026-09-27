#!/bin/bash
# Sends a GET request and prints the body only if the final status code is 200
[ "$(curl -s -L -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s -L "$1"
