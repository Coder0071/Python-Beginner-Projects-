#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to Computer Quiz!")

name = input("Enter your Name: ")
score = 0


play=input("Hello, Do you like to take a Quiz? ")
if play.lower()!="yes":
    quit()
else:
    print("Great! Let's Play Quiz! 😊")

answer= input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("correct ✔")
    score+=1
else:
    print("Incorrect ❌")

answer= input("What does GPU stands for? ")
if answer.lower()=="graphic processing unit":
    print("correct ✔")
    score+=1
else:
    print("Incorrect ❌")

answer= input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print("correct ✔")
    score+=1
else:
    print("Incorrect ❌")


answer= input("What does PSU stands for? ")
if answer.lower()=="power supply unit":
    print("correct ✔")
    score+=1
else:
    print("Incorrect ❌")


print(str(name)+" "+"Your total score is"+" "+str((score/4)*100))

