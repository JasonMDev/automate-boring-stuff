#! /usr/bin/python3
# wbScraper.py - DOwnload file from website and saves to file.
# TODO: Get address from clipboard.

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
len(res.text)
res.status_code == requests.codes.ok
print(res.text[:250])
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()


