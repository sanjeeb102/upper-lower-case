#!/usr/bin/env python
# coding: utf-8

# In[1]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in s:
        if(i.isupper()):
           d["UPPER_CASE"]+=1
        elif (i.islower()):
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# In[ ]:




