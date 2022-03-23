#!/usr/bin/env python
# coding: utf-8

# ### Python Primitive Data Structure
# 
# Strings, Lists, Tuples, Sets, Dicts

# ### Sequences: String, List, Tuple

# #### indexing
# access any item in the sequence using its index  
# 
# indexing starts with 0 for the first element

# In[2]:


# string

x = 'kosam'
print(x[3])

# list
y = ['Pig', 'cow', 'horse']
print(y[1])

# tuple
tup = ('Kevin', 'niklas', 'jenny', 'Craig')
print(tup[2])


# #### slicing
# slice out substring, sublist, subtuple using indexes  
# 
# [start: end+1: step]

# In[4]:


x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])


# #### adding & concatenating  
# combine 2 sequences of the same type by using +

# In[7]:


# string

x = 'house' + 'keeper'
print(x)

# list
y = ['pig', 'cow'] + ['horse']
print(y)

#tuple
z = ('Kevin', 'Niklas', 'Jenny') + ('Craig',)
print(z)


# #### multiplying  
# multiply a sequence using *

# In[8]:


# string
x = 'bug' * 3
print(x)

# list
y = [8, 5] * 3
print(y)

# tuple 
z = (2,4) * 3
print(z)


# #### checking membership  
# test whether an item is or is not in a sequence

# In[9]:


# string 

x = 'bug'
print('u' in x)

# list
y = ['pig', 'cow', 'horse']
print('cow' not in y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print('Niklas' in z)


# #### iterating  
# iterating through the items in a sequence

# In[11]:


# item
x = [7, 8, 3]
for item in x:
    print(item)
    
# index & item
y = [9, 8, 5, 4]
for index, item in enumerate(y):
    print(index, item)    


# #### number of items  
# count the number of items in a sequence
# 

# In[13]:


# string
x = 'bug'
print(len(x))

# list
y = ['pig', 'cow', 'horse']
print(len(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(len(z))


# #### minimum  
# find the minimum items in a sequence lexicographically.  
# Alpha or numeric, but cannot mix types

# In[14]:


# string
x = 'bug'
print(min(x))

# list
y = ['pig', 'cow', 'horse']
print(min(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(min(z))


# #### maximum  
# find the maximum items in a sequence lexicographically.
# Alpha or numeric, but cannot mix types

# In[15]:


# string
x = 'bug'
print(max(x))

# list
y = ['pig', 'cow', 'horse']
print(max(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(max(z))


# #### sum  
# find the sum if items in a sequence.  
# Entire sequence must be numeric

# In[18]:


# string ---> error
# x = [5, 7, 'bug']
# print(sum(x))   # generate an error

# list
y = [2,5,8, 12]
print(sum(y))
print(sum(y[-2:]))

# tuple
z = (50, 4,7, 19)
print(sum(z))
print(sum(z[-2:]))


# #### sorting  
# return a new list of items in sorted order  
# Does not change the original list

# In[19]:


# string
x = 'bug'
print(sorted(x))

# list
y = y = ['pig', 'cow', 'horse']
print(sorted(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z))


# #### sorting  
# sort by second letter  
# Add a key parameter and lamba function to return the second character  
# (the word key here is defined parameter name, k is an arbitrary variable name)

# In[20]:


z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z, key=lambda k: k[1]))


# #### count(item)  
# return count of an item

# In[21]:


# string
# string
x = 'hippo'
print(x.count('p'))

# list
y = ['pig', 'cow', 'horse', 'cow']
print(y.count('cow'))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.count('Kevin'))


# #### index(item)  
# returns the index of the first occurence of an item

# In[22]:


# string
x = 'hippo'
print(x.index('p'))

# list
y = ['pig', 'cow', 'horse', 'cow']
print(y.index('cow'))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.index('Kevin'))


# #### unpacking  
# unpacking the n items of a sequence into n variables

# In[23]:


x = ['pig', 'cow', 'horse']
a, b, c = x
print(a, b, c)


# ### Lists  
# 
# 
# * General purpose
# * Most widely used data structure
# * Grow and shrink size as needed
# * Sequence type
# * sortable

# #### constructors  
# creating a new list

# In[25]:


x = list()
y = ['a', 25, 'dog', 8.43]
tuple1 = (10, 20)
z = list(tuple1)

# list comprehension
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i > 4]
print(b)


# #### delete  
# delete a list or an item in a list

# In[28]:


x = [5, 3, 8, 6]
del(x[1])
print(x)
del(x)


# #### append  
# append an items to end of a list

# In[29]:


x = [5, 3, 8, 6]
x.append(7)
print(x)


# #### extend  
# append a sequence to a list (similar to + method)  
# combining separate list into one list

# In[33]:


x = [5, 3, 8, 6]
y = [12,15]
x.extend(y)
print(x)


# #### insert  
# insert an item at a given index

# In[34]:


x = [5, 3, 8, 6]
x.insert(1, 7)
print(x)

x.insert(1, [7,8])
print(x)


# #### pop  
# pop last item off the list and return item

# In[35]:


x = [5,3,8,6]
x.pop()
print(x)
print(x.pop())


# #### remove  
# remove the first instance of an item

# In[37]:


x = [5, 3,8,6,3]
x.remove(3)
print(x)


# #### reverse  
# reverse the order of list.  
# It is an in-place sort, meaning it changes the original list

# In[39]:


x = [5, 3,8,6,3]
x.reverse()
print(x)


# #### sort  
# sort the list in place  
# Note:  
#     sorted(x) return a new sorted list without changing the original list x  
#     x.sort() puts the items of x in sorted order (sorts in place)

# In[40]:


x = [5,3,8,6]
x.sort()
print(x)


# #### reverse sort  
# sort items descending  
# use reverse=True parameter to the sort function

# In[41]:


x = [5,3,8,6]
x.sort(reverse=True)
print(x)


# ### Tuples  
# * Immutable (can't add/change)
# * Useful for fixed data
# * Faster than lists
# * Sequence type
#              

# #### constructors  
# creating new tuples

# In[43]:


x = ()
x = (1,2,3)
x = 1,2,3
x = 2, # the comma tells python it's a tuple
print(x, type(x))

list1 = [2,3,4]
x = tuple(list1)
print(x, type(x))


# #### tuple are immutable  
# but member objects may be mutable

# In[46]:


x = (1,3,5,6)
# del(x[1]) # fails
# x[1] = 7  # fails
print(x)

y = ([1,2], 4)   # tuple where first item is a list
del(y[0][1])     # delete the 2
print(y)          # the list within the tuple is mutable

y += (9,)   # concatenating two tuple  works
print(y)


# ### Sets  
# * stroes non-duplicate items
# * very fast access vs Lists
# * greate for checking membership
# * Math set ops (union, interset)
# * Sets are unordered (cannot sort a set)

# #### constructors  
# creating new sets

# In[48]:


x = {3,4,5,6,9}
print(x)

y = set()
print(y)

list1 = [2,5,5,7,7]
z = set(list1)
print(z)


# #### set operations

# In[51]:


x = {3, 8, 5}
print(x)

# add
x.add(7)
print(x)

# remove
x.remove(3)
print(x)

# get length of set x
print(len(x))

# check membership in x
print(5 in x)

# pop random items from set x
print(x.pop(), x)

# delete all items from set
x.clear()
print(x)


# #### Mathematical set Operations  
# intersection (AND): set1 & set2  
# union (OR): set1 | set2  
# symmetric difference (XOR): set1 ^ set2  
# difference (in set1 but not set2): set1 - set2  
# subset (set2 contains set 1): set1 <= set2  
# superset (set1 contains set2): set1 >= set2

# In[52]:


s1 = {1,2,3}
s2 = {3,4,5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)


# ### Dictionaries (dict)  
# * key/value pairs
# * associative array, like Java HashMap, JavaScript Objects  
# * Dicts are unordered

# In[56]:


x = {'pork': 25.3, 'beef': 50.8, 'chicken': 22.7}
print(x)
x = dict([('pork', 25.3), ('beef', 50.8), ('chicken', 22.7)])
print(x)
x = dict(pork=25.3, beef=50.8, chicken=22.7)
print(x)
# x = dict()
# print(x)


# #### dict operations

# In[57]:


# add or update
x['shrimp'] = 38.2  
print(x)

# delete an item
del(x['shrimp'])
print(x)

# get length of dict
print(len(x))

# delete all items from dict x
x.clear()
print(x)

#delete dict x
del(x)


# #### accessing keys and values in a dict  
# Not compatible with Python2

# In[59]:


y = {'pork': 22.3, 'beef': 22.5, 'chicken': '22.7'}
print(y.keys())
print(y.values())
print(y.items())   # key value pairs

# checking membership in y_keys (only looks in keys not values)
print('beef' in y)

# check membership in y_values
print('claims' in y.values())


# #### iterating a dict  
# Note items are in random order

# In[61]:


for key in y:
    print(key, y[key])
    
for key, value in y.items():
    print(key, value)

