#!/bin/bash
# Sends an OPTIONS request and displays the HTTP methods the server accepts
curl -s -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
