#!/usr/bin/env python
# coding: utf-8

# ## Heap Or Binary Heap

# ## Types
# 
# * MaxHeap ---> every node is <= parent
# * MinHeap ----> evry node is => parent

# ## MaxHeap
# 
# * Complete Binary Tree
# * Every node <= its parent

# ## MaxHeap is Fast
# * Insert in O(log n)
# * Get Max in O(1)
# * Remove Max in O (log n) 

# ### Easy to implement using a List
# 
# First items in the list is the max heap root  
# parent(i) = i/2  
# left = i * 2  
# right = i * 2 + 1

# In[2]:


print([1, 2,3,4,5,6,7,8,9,10])
print([25,16,24,5,11,19,1,2,3,10])


# ### MaxHeap Operation
# * push (insert)
# * peek (get max)
# * pop (remove max)

# ### Push
# * add value to the end of array
# * float it up to its proper position

# ### Peek
# * return the value at heap(1)

# ### Pop
# * move the max to the end of array
# * Delete it
# * Bubble down the item at index 1 to its proper position
# * return max

# ## MaxHeap
# 
# A MaxHeap always bubble the highest value to the top, so it can removed instantly  
# Public functions push, peek, pop  
# Private functions __swap, __float_up, __bubble_down, __str  
# underlying data structure is List  
# elements start at index 1 and not 0

# In[12]:


class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__float_up(len(self.heap)-1)
            
            
    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) -1)
        
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return None
    
    
    def pop(self):
        if len(self.heap) == 2:
            max = self.heap.pop()
        elif len(self.heap) > 2:
            self.__swap(1, len(self.heap) -1)
            max = self.heap.pop()
            self.__bubble_down(1)
        else:
            max = False
        return max
    
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    
    def __float_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)
            
            
    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)
            
            
    def __str__(self):
        return str(self.heap)
            
        


# ## MaxHeap Test Code

# In[16]:


maxHeap = MaxHeap([1, 8, 9, 12, 11, 25, 32, 41])
maxHeap.push(10)
maxHeap.push(103)
print(maxHeap)
print(maxHeap.pop())
print(maxHeap.peek())


# ## MinHeap  
# * Complete Binary Tree
# * Every node >= its parent

# ## Easy to Implement using List  
# 
# First items in the list is the min heap root  
# parent(i) = i/2  
# left = i * 2  
# right = i * 2 + 1  
# 

# In[17]:


print([1, 2, 3, 4, 5, 6, 7, 8, 9,10])
print([1, 5, 11, 1, 24, 19, 16, 2, 3, 10])


# ### MinHeap Operation
# * push (insert)
# * pop (remove min )
# * peek (get min)

# ### Push
# * add value to the end of array
# * float it up to its proper position

# ### Peek
# * return the value at heap(1)

# ### Pop
# * move the min to the end of array
# * Delete it
# * Bubble down the item at index 1 to its proper position
# * return min

# ### MinHeap
# A MinHeap always bubble the lowest value to the top, so it can removed instantly  
# Public functions push, peek, pop  
# Private functions __swap, __float_up, __bubble_down, __str  
# underlying data structure is List  
# elements start at index 1 and not 0

# In[18]:


class MinHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__float_up(len(self.heap)-1)
            
            
    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) -1)
        
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return None
    
    
    def pop(self):
        if len(self.heap) == 2:
            min = self.heap.pop()
        elif len(self.heap) > 2:
            self.__swap(1, len(self.heap) -1)
            min = self.heap.pop()
            self.__bubble_down(1)
        else:
            min = False
        return min
    
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    
    def __float_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)
            
            
    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] > self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] > self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)
            
            
    def __str__(self):
        return str(self.heap)


# ### MinHeap Test Code

# In[19]:


minHeap = MinHeap([10, 8, 9, 12, 11, 25, 32, 41])
minHeap.push(10)
minHeap.push(103)
print(minHeap)
print(minHeap.pop())
print(minHeap.peek())

