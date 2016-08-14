#! /usr/bin/python3
# pw.py - An insecure password locker program.

PASSWORDS = { 'email': 'FghjhgduY&^%34$98', 
              'blog': 'djhgjdhg7678adhb',
              'luggage': 'eytuey4174e35'
}

import sys, pyperclip
if len(sys.argv) < 2:
  print('Usage: python pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1] # first comand line arg is the account name

if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print('Password for ' + account + ' copied to clipboard.')
else: