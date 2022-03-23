#!/usr/bin/env python
# coding: utf-8

# # Stacks

# stack is a Last In First Out (LIFO) data structure
# 
# push an item onto the stack
# 
# pop an item off the stack
# 
# peek - get item on top of stack without removing it
# 
# clear - all items from stack
# 
# All push and pop operations are to/from the top of the stack
# 
# The ONLY way to remove the bottom/first item of the stack is to remove all on top items first

# ### stacks use case 
# Undo - track which commands have been executed.  
# Pop last command off command stack to undo it

# ### Stack using Python List  
# Stack is a LIFO data structure --- last in, first out  
# Use append() to push an item onto the stack  
# use pop() to remove an item

# In[2]:


my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack)


# In[3]:


print(my_stack.pop())
print(my_stack.pop())
print(my_stack)


# ### Stack using List with a Wrapper Class  
# We create a Stack class and full set of Stack methods
# But the underlying data structure is really a Python List  
# For pop and peek methods we first check whether the stack is empty to avoid exceptions

# In[4]:


class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) -1]
        else:
            return None
        
    def __str__(self):
        return str(self.stack)


# ## Test Code for Stack Wrapper Class

# In[6]:


custom_stack = Stack()
custom_stack.push(1)
custom_stack.push(10)
custom_stack.push(11)
print(custom_stack)
print(custom_stack.pop())
print(custom_stack.peek())
print(custom_stack.pop())
print(custom_stack.pop())
print(custom_stack.pop())

