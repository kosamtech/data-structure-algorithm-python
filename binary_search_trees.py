#!/usr/bin/env python
# coding: utf-8

# ## Binary Trees

# ## Component
# 
# * Node ---> each part of a tree is called a node
# * Edges ---> each connection to the node is called edge
# * Root ----> at the very top of tree we got root node
# * Parent ---> a parent can have at most 2 children
# * Child ---> left and right child node
# * Sibling ---> node with same parent are called sibling nodes
# * Leaf  ---> very bottom node with no child are called leaf nodes
# * subtree ---> subtree connects to root node
# * ancestors ---> parents of leaf nodes
# * descendants ---> every node below the root node
# 
# ## Binary Search Trees
# * each node is greater than every node in its left subtree
# * each node is less than every node in its right subtree

# ## Binary Search Tree Operations
# * insert
# * find
# * delete
# * get_size
# * traversals

# ### Insert
# * start at root
# * always insert as a leaf

# ### Find
# * start at root
# * return the data if found, or False if not found

# ### Delete
# 3 possible cases
# * leaf node -----> just delete the leaf node; does not affect other nodes
# * 1 child ---> promote the child to the target node's position
# * 2 children ---> find the next higher node; swap the node then delete

# ### Get_size
# returns number of nodes  
# works recursively
# size = 1  
# * +size (left subtree)
# * +size (right subtree)

# ### Traversals
# 
# #### Preorder traversal
# visit root before visiting the root's subtrees
# 
# #### inorder traversal
# visit root between visiting the root's subtrees  
# gives value in sorted order (bottom left most node to right most node)

# ### Advantanges of Binary Search Trees
# 
# because trees use recursion for most operations, they are faily easy to implement  
# speed is fast   
# insert, delete, find in O(h) = O(log n)  
# In balances bst with 10,000,000 nodes it takes 30 comparison!

# ## Binary Search Tree
# **constructor** sets three attributes; data. left subtree, and right subtree.  
# **insert** inserts a new subtree into the proper location  
# **find** finds a value; if value not found, returns False  
# **get_size** returns the number of nodes in the tree (excluding None nodes)  
# **preorder** prints a preorder traversal of the tree  
# **inorder** prints an inorder traversal of the tree  
# 

# In[1]:


class BinarySearchTree:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
        
    def insert(self, data):
        if self.data == data:
            return False # duplicate value
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)
                return True
            
            
    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
            
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1
        
    
    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()
                
    
    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data, end=' ')


# ## Test Code
# 
# We create a new tree, insert one value, insert a whole list of values, find all values from 1 to 15  
# (False for 0, 5,8 shows that those values are not in the tree), print the size of the tree, print preorder, inorder and post order traversals
# 

# In[3]:


bst = BinarySearchTree(7)
bst.insert(9)
for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
    bst.insert(i)
    
for i in range(16):
    print(bst.find(i), end=' ')
    
    
print('\n', bst.get_size())

bst.preorder()
print()
bst.postorder()
print()
bst.inorder()
print()

    

