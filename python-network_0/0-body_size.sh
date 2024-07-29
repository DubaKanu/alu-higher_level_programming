#!/bin/bash
<<<<<<< HEAD
# Get the byte size of the HTTP response header for a given URL.
curl -s "$1" | wc -c
=======
# ends a request to that URL displays the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
>>>>>>> fd21f878a9e58df51c5296e536c70c0570998fad
