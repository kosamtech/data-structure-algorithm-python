#!/usr/bin/env python
# coding: utf-8

# ## Queue

# #### Enqueue  
# add an item to the end of the line
# 
# #### Dequeue
# remove an item from front of the line
# 
# Queue is a First In First Out (FIFO) data structure
# 
# Enqueue on one end, and Dequeue from the other end

# ## Queues Use Cases  
# Queues are good for modeling anything you wait in line for  
# Bank tellers.  
# Placing an order at MCDonals  
# DMV customer service  
# Supermarket checkout

# ## Queue Using Python Deque
# Queue is FIFO data structure --- first in first out  
# Deque is double-ended queue, but we can use it for our queue  
# We use append() to enqueue an item and popleft to dequeue an item  
# 
# 

# In[11]:


from collections import deque
my_queue = deque()
# help(my_queue)
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
print(my_queue)
print(my_queue.popleft())
print(my_queue)


# ## Queue using Deque with a Wrapper Class

# In[5]:


from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
        
    
    def enqueue(self, item):
        self.queue.append(item)
        
    
    def dequeue(self):
        return self.queue.popleft()
    
    def __str__(self):
        return str(self.queue)


# In[7]:


custom_queue = Queue()
custom_queue.enqueue(45)
custom_queue.enqueue(2)
custom_queue.enqueue(23)
custom_queue.enqueue(12)
print(custom_queue)
print(custom_queue.dequeue())
print(custom_queue)
print(custom_queue.dequeue())
print(custom_queue)
print(custom_queue.dequeue())
print(custom_queue)
print(custom_queue.dequeue())
print(custom_queue)

