#! /usr/bin/python3
# bulletPointAdder.py - Adds WIki bullet points to the start
# of each line of text to the clipbaord.

import pyperclip
text = pyperclip.paste()

# Separate line and add stars.
lines = text.split('/n')
for i in range(len(lines)):     # loop through all indexes in the "line" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list

text = '/n'.join(lines)

pyperclip.copy(text)

print(text)