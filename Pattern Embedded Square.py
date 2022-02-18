#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main_algo():
    n = int(input("Enter the value for the structure to be built: "))
    for i in range(1, n + 1):  
        for j in range(1, n + 1):  
            if(i < j):
                min =i
            else:
                min=j
            print(n - min + 1, end = " ")  
  
        for j in range(n - 1, 0, -1):  
            if(i < j):
                min=i
            else:
                min=j
            print(n - min + 1, end = " ") 
  
        print() 
      
    for i in range(n - 1, 0, -1):  
        for j in range(1, n + 1):  
            if(i < j):
                min=i
            else:
                min=j
            print(n - min + 1, end = " ")  
  
        for j in range(n - 1, 0, -1):  
            if(i < j):
                min=i
            else:
                min=j
            print(n - min + 1, end = " ") 
  
        print() 


# In[4]:


main_algo()


# In[ ]:




