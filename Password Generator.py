#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
l='qwertyuiopasdfghjklzxcvbnm'
u='QWERTYUIOPASDFGHJKLZXCVBNM'
n='1234567890'
s='[]{}()*&$@._'
all=l+u+n+s
#For which platform you need to generate password
# Example= Facebook,google,gmail etc.
platform=input("Password for: ")
#Enter length of the password
length=int(input("Password Length: "))
password="".join(random.sample(all,length))
print("Your password for "+platform+":",password)


# In[ ]:




