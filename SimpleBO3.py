#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
heads = 0
tails = 0
headWin = 0
tailWin = 0
cfm = 0
finish = 0
decider = 0

def coinFlip():
    global heads
    global tails
    while 1:
        num1 = random.randint(1, 100)
        if num1 % 2 == 0:
            tails += 1
        elif num1 % 2 == 1:
            heads += 1
        break
            
def coinFlipCfm():
    numF = 0
    numS = 0
    while 1:
        numF = random.randint(1, 100)
        numS = random.randint(1, 100)
        numF = numF % 2
        numS = numS % 2
        if numF == 0 and numS == 0:
            continue
        elif numF == 0 and numS == 1:
            return 2
        elif numF == 1 and numS == 0:
            continue
        elif numF == 1 and numS == 1:
            return 1
        
def checkRound():
    global heads
    global tails
    global headWin
    global tailWin
    if heads == 2:
        headWin += 1
        heads = 0
        tails = 0
    elif tails == 2:
        tailWin += 1
        heads = 0
        tails = 0

def confirmFlip():
    global headWin
    global tailWin
    global cfm
    if headWin == 2:
        print("Yes wins 'Best Of 3'")
        cfm = cfm + 1
    elif tailWin == 2:
        print("No wins 'Best Of 3'")
        cfm = cfm + 0

        
while finish == 0:
    if headWin == 2 or tailWin == 2:
        print("heads: " + str(headWin))
        print("tails: "+ str(tailWin))
        confirmFlip()
        decider = coinFlipCfm()
        if decider == 0:
            heads = 0
            tails = 0
            headWin = 0
            tailWin = 0
            cfm = 0
            finish = 0
            decider = 0
        elif decider == 1:
            finish = 1
            print("Yes wins decider")
            cfm = cfm + 1
            break
        elif decider == 2:
            finish = 0
            print("No wins decider")
            print("Restarting...")
            print("______________________________________________________________________________________________________")
            heads = 0
            tails = 0
            headWin = 0
            tailWin = 0
            cfm = 0
            finish = 0
            decider = 0
            cfm = cfm + 0
            
    coinFlip()
    checkRound()
    
if cfm == 2:
    print("")
    print("Pick Yes")
elif cfm == 1:
    print("")
    print("Pick No")
    


# In[ ]:




