#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
guess=0

print("Number Guessing Game")

top_of_range=input("Type a Number: ")

if top_of_range.isdigit():  #check for Entered values is digit or not.
    top_of_range=int(top_of_range) #convert it to integer
    
    if top_of_range <= 0:
        print("Please Enter Number Greater than 0")
        quit()
randomnum= random.randint(-10,top_of_range)

# Take Guesses from User 
while True: 
    guess+=1
    user_guess=input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number")
        continue
    
    if user_guess == randomnum:
        print("You Got it!!!")
        break
    elif user_guess > randomnum: 
            print("You were above the Number!!!")
    else:
            print("You were below the Number!!!")
        
print("You got it in",guess,"Guesses")
    


# In[ ]:




