#!/usr/bin/env python
# coding: utf-8

# ### Python List Comprehension  
# basic format: new_list = [transform sequence [filter]]

# In[1]:


import random


# #### get values within a range

# In[2]:


under_10 = [x for x in range(10)]
print('under_10:' + str(under_10))


# #### get_squared values

# In[3]:


squared = [x**2 for x in under_10]
print('squares' + str(squared))


# #### get odd numbers using mod

# In[4]:


odds = [x for x in range(10) if x%2 == 1]
print('odds' + str(odds))


# #### get multiple of 10

# In[6]:


multiples = [x*10 for x in range(10)]
print('multiples' + str(multiples))


# #### get all numbers from a string

# In[7]:


s = 'I love 2 go t0 the store 7 times a w3ek'
nums = [x for x in s if x.isnumeric()]
print('nums: ' + str(nums))


# #### get index of a list item

# In[9]:


names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
index = [k for k, v in enumerate(names) if v == 'Anu']
print(index)
print('index: ' + str(index[0]))


# #### delete an item from a list

# In[10]:


letters = [x for x in 'ABCDEFGHIJKLMNO']
random.shuffle(letters)
letrs = [x for x in letters if x != 'C']
print(letters, letrs)


# ####  if-else condition in comprehension  
# must come before iteration

# In[11]:


nums = [5,3,10,18,6,7]
new_list = [x if x%2 == 0 else 10*x for x in nums]
print('new_list: ', new_list)


# #### nested loops for 2D list  
# b is the subset, x is the values

# In[13]:


a = [[1,2], [3,4]]
new_list = [x for b in a for x in b]
print(new_list)


# In[ ]:




