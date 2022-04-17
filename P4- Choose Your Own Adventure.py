#!/usr/bin/env python
# coding: utf-8

# In[20]:


name= input("Enter Your Name!")
print("Welcome,",name,"to this Adventure🤪")

answer=input("Your are on dirt road, It has come to an end & You can go Left or Right. Which way would you like to go? ").lower()

if answer == "left":
    answer= input("You come to a river!!!, you can walk around it or you can swim across? ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator 😥")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost game!!!")     
    else:
        print("Not a valid option, You lose.")   
        
elif answer == "right":
    answer= input("You come to a Bridge!!!, It looks Wobbly, do you cross it or head back (cross/back?) ").lower()
    
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer=input("You crossed the bridge and meet a stranger. Do you like to talk to them? (yes/no)? ")
        if answer == "yes":
            print("You talk to stranger they gave you gold, you WIN!!!😎🥇💥")
        elif answer == "no":
            print("You Ignored them!!!")     
        else:
            print("Not a valid option, You lose.")   
    else:
        print("Not a valid option, You lose.")   

else:
    print("Not a valid option, You lose.")


# In[ ]:




