#!/usr/bin/python
""" Create ansible yaml lines to create users with CSCfi.ansible-role-users
Usage: python create_passwords.py > host_vars/etherpad_node/vault.yml

https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

Use at your own risk. Do encrypt things.

Usage:

$ python create_passwords.py > host_vars/etherpad_node/vault.yml

"""
import random
import string
from passlib.hash import sha512_crypt # pylint: disable=import-error

N = 6
USERS = 15

BASEUID = 10000

print "moreusers:"
for user in range(0, USERS):

    useruid = BASEUID + user

    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

    encrypted = sha512_crypt.using(rounds=5000).hash(password)

    #print "%s: %s" %(password, encrypted)
    # print in ansible format..
    print " - {name: ansible%s, state: 'present', uid: %s, group: 'ansibleusers', shell: '{{adminshell}}', password: '%s', generate_ssh_key: 'yes' } # %s" %(user, useruid, encrypted, password) # pylint: disable=line-too-long
