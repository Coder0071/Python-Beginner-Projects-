#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import random

user_wins=0
computer_wins=0
options= ["rock","paper", "scissor"]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
        
    random_num= random.randint(0,2)
    # rock:0 , paper:1, scissor:2
    computer_pick=options[random_num]
    print("Computer Picked",computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissor":
        print("You Won")
        user_wins+=1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_wins+=1
      
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won")
        user_wins+=1
        
    else:
        print("You Lost")
        computer_wins+=1
    
print("You Won!!!",user_wins,"Times")    
print("computer Won!!!",computer_wins,"Times")    
print("GoodBye!!!")


# In[ ]:




