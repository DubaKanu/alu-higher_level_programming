#!/usr/bin/python3
import requests

# Fetching the status from the given URL
response = requests.get('https://alu-intranet.hbtn.io/status')

# Displaying the body of the response
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
