#!/usr/bin/env python
# coding: utf-8

# In[9]:


from cryptography.fernet import Fernet
def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key
master_pwd = input("Enter the master password: ")
key= load_key() +  master_pwd.encode()
fer=Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def view():
    with open("passwords.text","r") as f:
        for line in f.readlines():
            data= line.rstrip()
            user, passw = data.split("|")
            print("User:",user, "| Password:",str(fer.decrypt(passw.encode())).decode())

def add():
    name = input("Account Name: ")
    pwd =input("Password: ")
    
    with open("passwords.text","a") as f:
        f.write(name+ " | " +fer.encrypt(pwd.encode()).decode() + "\n")
        
        
while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add), Q to Quit ").lower()
    if mode== "q":
        break
    
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid Mode.")
        continue


# In[1]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




