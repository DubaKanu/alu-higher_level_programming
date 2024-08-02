#!/usr/bin/python3
"""__summary__
- Write a Python script that fetches https://alu-intranet.hbtn.io/status
- using the urllib package.
"""
import urllib.request

url = 'https://intranet.hbtn.io/status'
if url.startswith('https://'):
    url = 'https://alu-intranet.hbtn.io/status'


if __name__ == '__main__':
    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content.decode('utf-8')))
