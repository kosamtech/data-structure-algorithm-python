#!/usr/bin/env python
# coding: utf-8

# ## LinkedList

# * Every Linked List has a component called node
# * Every Node has 2 parts; data and a pointer to the next node
# 
# * You can store any valid data type as data
# * The very front node is root node
# * Last node is tail
# 
# * 2---->3----->None

# ### Attributes
# root - pointer to the begining of the list  
# size - number of nodes in list  
# tail - ??

# ## Types
# * Standard or Regular Linked List
# * Circular Linked List
# * Doubly Linked List

# ### Operations
# * find(data)
# * add(data)
# * remove(data)
# * print_list()

# ## Python Linked Lists

# ## Node Class
# Node class has a constructor that sets the data passed in, and optionally can  
# have next_node and prev_node  
# It also has a str method to give a string representation for printing  
# Note that prev_node is only used for Doubly Linked Lists

# In[1]:


class Node:
    
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
        
    
    def __str__(self):
        return (f'({self.data})')


# ## LinkedList Class
# A LinkedList object has two attributes; a root node that defaults to None and size that defaults 0
# 
# **Add** method receives a piece of data, creates a new Node, setting the root as current Node and changes the LL's root pointer to the new node and increments size
# 
# **Find** iterates through the node until it finds the data passed in. if it finds the data it will return it. otherwise returns None
# 
# **Remove** needs pointers to this_node and prev_node. If it finds the data, it needs to check if it is in the root node (prev_node is None) before deciding how to bypass the deleted node
# 
# **Print_list** iterates the list and prints each node

# In[2]:


class LinkedList:
    
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        
        
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
        
        
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    
    
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None: # data is in non-root
                    prev_node.next_node = this_node.next_node
                else: # data is in root node
                    self.root = this_node.next_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False # data not found
    
    
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='--->')
            this_node = this_node.next_node
        print('None')


# ## Regular LinkedList Test Code
# 
# This test code adds to the linkedlist, prints the list, print size, remove an item and finds an ite,

# In[3]:


linkedlist = LinkedList()
linkedlist.add(5)
linkedlist.add(16)
linkedlist.add(12)
linkedlist.print_list()

print('size = ', str(linkedlist.size))
print(linkedlist.remove(5))
linkedlist.print_list()
print('size = ', str(linkedlist.size))
linkedlist.add(3)
linkedlist.add(7)
linkedlist.print_list()
print('size = ', str(linkedlist.size))
print(linkedlist.root)


# ## Circular Linked List
# 
# Unlike the regular linkedlist instead of having a null pointer, the tail node points back to the root node
# 
# **add** operation in circular linked list works slightly different; the new node is added as the second node and not root node
# 
# **Advantage** over regular (singly) linked list
# * Ideal for modeling continuous looping objects, such as Monopoly board or a race track
# 
# Include attributes root and size  
# Include methods add, find, remove and print list

# In[36]:


class CircularLinkedList:
    
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        
    
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1
    
    
    def find(self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node
            
            
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while True:
            if this_node.data == d: # found
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True # data removed
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node
            
    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='--->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end='--->')
            


# ### Circular Linked List Test Code

# In[37]:


cll = CircularLinkedList()
for i in [5,7,8,3,9]:
    cll.add(i)
       
print('size = ', cll.size)
print(cll.find(8))
print(cll.find(12))

my_node = cll.root
print(my_node, end='--->')
for i in range(8):
    my_node = my_node.next_node
    print(my_node, end='--->')


# In[38]:


cll.print_list()
cll.remove(8)
print(cll.remove(15))
print('size = ', cll.size)
cll.remove(5)
cll.print_list()


# ## Doubly Linked List
# 
# Every node has 3 parts; **data** and pointers to **previous** and **next** nodes  
# 
# Delete operation works slighty different with doubly linked list  
# * note prev_node next_node  
# * next_node prev_node  
# * prev.next = this.next  
# * next.prev = this.prev
# 
# **Advantage** over regular (singly) linked list
# * can iterate the list in either direction
# * can delete a node without iterating thought the list (if given a pointer to the node)
# 
# has an extra attribute called last

# In[4]:


class DoublyLinkedList:
    
    def __init__(self, r = None):
        self.root = r
        self.last = r
        self.size = 0
        
        
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1
        
        
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next_node == None:
                return False
            else:
                this_node = this_node.next_node
                
                
    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None: # delete a middle node
                        this_node.prev_node.next_node = this_node.next_node.prev_node
                        this_node.next_node.prev_node = this_node.prev_node.next_node
                    else: # delete last node
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else: #delete root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True # data removed
            else:
                this_node = this_node.next_node
        return False # data not found
    
    
    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='--->')
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end='--->')
            
            


# ## Doubly Linked List Test Code

# In[13]:


dll = DoublyLinkedList()
for i in [5,9,3,8,9, 11,12,7]:
    dll.add(i)
    
print('size = ', dll.size)
dll.print_list()
dll.remove(8)
print('size = ', dll.size)


# In[14]:


print(dll.remove(15))
print(dll.find(15))
dll.add(21)
dll.add(22)
dll.remove(5)
dll.print_list()
print(dll.last.prev_node)

