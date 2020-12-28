#!/usr/bin/env python
# coding: utf-8

# In[40]:


import time
import threading 
from threading import*

json_dict={} # for data storage I used json_dict

#for create operation 
def create(key,value,halt=0):
    if key in json_dict:
        print("error:key already exists") #error
    else:
        if(key.isalpha()):
            if len(json_dict)<(1024*1020*1024) and value<=(16*1024*1024): #file size less than 1GB and Jasonobject value less than 16KB 
                if halt==0:
                    dt=[value,halt]
                else:
                    dt=[value,time.time()+halt]
                if len(key)<=32:
                    json_dict[key]=dt
            else:
                print("Memory limit reached")
        else:
            print("Invalid.it must contain only alphabets")

#for read operation            
def read(key):
    if key not in json_dict:
        print("Please enter a valid key") 
    else:
        n=json_dict[key]
        if n[1]!=0:
            if time.time()<n[1]: 
                stri=str(key)+":"+str(n[0]) 
                return stri
            else:
                print("time-to-live",key,"has expired") 
        else:
            stri=str(key)+":"+str(n[0])
            return stri
#for delete operation         
def delete(key):
    if key not in json_dict:
        print("Please enter a valid key") 
    else:
        n=json_dict[key]
        if n[1]!=0:
            if time.time()<n[1]:
                del json_dict[key]
                print("key deleted")
            else:
                print("time-to-live",key,"has expired") 
        else:
            del json_dict[key]
            print("key deleted ")
            


# In[44]:


create("Shiraz",22)
create("Hussain",80) 
read("Shiraz")
#returns the value of the respective key in Jasonobject format 
read("Hussain")
#returns the value of the respective key in Jasonobject format

create("Shiraz",60)
delete("Shiraz")
delete("hussain")
read("Hu")
#using multiple threads
t1=threading.Thread(target=(create or read or delete),args=("Shiraz", 22))
t1.start()
t2=threading.Thread(target=(create or read or delete),args=("Shiraz", 32)) 
t2.start()
t3=threading.Thread(target=(create or read or delete),args=("hussain", 42))
t3.start()
t1.join()
t3.join()
t2.join()


# In[ ]:




