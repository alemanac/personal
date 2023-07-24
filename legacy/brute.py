#!/usr/bin/env python

#import TMod
import random
import time

#TMod.setup()
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#'
password = ''


def randompass():
    global password
    num = 1
    howlong = input('how long>>> ')
    try:
        howlong = int(howlong)
    except:
        howlong = 4
    password = random.choice(char)
    while num != howlong:
        addc = random.choice(char)
        password = password + addc
        num = num + 1
    return password


def ownpass(x):
    x = input('put ur pass>>> ')
    return 


def brute():
    global figpass
    import time
    global timee
    timee = 0
    figpass = ''
    addletter1 = 0
    guessright = 0
    while figpass != password:
        #TMod.clear()
        print(figpass)
        theletter = char[addletter1]
        if theletter == password[guessright]:
            guessright = guessright + 1
            figpass = figpass + theletter
            addletter1 = 0
        else:
            addletter1 = addletter1 + 1
            timee = timee + 1
            time.sleep(0.001)


choice = input('[random],[myown] which one>>> ')

if choice == 'myown':
    password = ownpass(password)
    brute()
    #TMod.clear()
    print(figpass)
    print('tries:', timee)
elif choice == 'random':
    randompass()
    brute()
    #TMod.clear()
    print(figpass)
    print('tries:', timee)
else:
    print('invalid choice')
