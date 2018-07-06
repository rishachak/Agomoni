#!/usr/bin/python
import os
import time

x=3
y=10

def printStage(m):
    for i in range(0,x-m,1):
        printLine(" ")
    for i in range(0,m,1):
        printLine("x")

def printLine(s):
    s1 = ""
    for i in range(0,y,1):
        s1 += s
    print s1
    print("\n")

while(1==1):
    printStage(1)
    time.sleep(0.5)
    os.system('clear')
    print("\n")
    printStage(2)
    time.sleep(0.5)
    os.system('clear')
    print("\n")
    printStage(3)
    time.sleep(0.5)
    os.system('clear')
    

