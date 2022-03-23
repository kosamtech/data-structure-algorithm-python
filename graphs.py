#!/usr/bin/env python
# coding: utf-8

# ## Graphs

# ### Components
# * vertices
# * edges

# ### Types
# * **Undirected Graphs** - relationship are 2 way; used to model social or computer network
# * **Directed graphs** - relationship are 1 way; used to model airplane flights or bus routes

# ### Modelling Graphs
# * Adjaceny List ---> list of neighours stored in each vertex
# * Adjaceny Matrx  ---> Matrix of neighbors stored centrally in Graphs Objects

# ### Adjaceny List
# 
# A: B,C,E  
# B: A,C  
# C: A, B, D, E  
# D: C  
# E: A, C  
# 

# ### Adjanceny Matrix
# 
# consist of from vertices and to vertices
# puts 0 where there is no edge and 1 where there is edege
# 
# [
#     [0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0],
#     [1, 1, 0, 1, 1],
#     [0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 0]
# ]
# 
# **weighted edges** much easier to implement with adjancency matrix; because of puting just 1  
# you can put the weight instead  
# for adjanceny list you have to include tuple for its weights
# 

# ### Which is better?
# Dense Graph -  
# graph where |E| = |v|2  
# 
# Sparse Graph -  
# graph where |E| = |v|
# 
# **Adjacency Matrix** takes up |V|2 spance regardless how dense the graph is  
# Matrix for a graph with 10000 vertices will take up at least 100000000 Bytes
# 
# **Adjaceny List**
# * Pro - Faster and uses less space for Sparse graphs
# * Con - Slower for Dense graphs
# 
# **Adjaceny Matrix**
# * Pro - Faster for Dense graphs
# * Pro - Simpler for weighted edges
# * Con - uses more space

# ### Graph Implementation Using Adjaceny List
# 
# for an undirected graph

# ### Vertex Class
# 
# The vertex class has a constructor that sets the name of the vertex (in our example just a letter), and creates a new empty set to store neighbours
# 
# 
# The add neighbor method adds the name of a neighboring vertx to the neighbor set. This set automatically eliminates duplicate

# In[1]:


class Vertex:
    
    def __init__(self, n):
        self.name = n
        self.neighbors = set()
        
        
    def add_neighbor(self, v):
        self.neighbors.add(v)
        
    


# ### Graph Class
# 
# The graph class uses a dictionary to store vertices in the format, vertex_name: vertex_object.  
#   
# Adding a new vertex to the grap, we first check if the object passed in is a vertex object, then we check if it  
# already exists in the graph. If both checks pass then we add the vertex to the graph's vertices dictionary.  
#   
# when adding an edge, we receive two vertex names, we first check if both vertex names are valid, then we add each   
# to the other's neighbors set  
#   
# To print the graph we iterate through the vertices, and print each vertex name (the key) followed by its sorted  
# neighbors list

# In[2]:


class Graph:
    
    vertices = dict()
    
    
    def __init__(self):
        pass
    
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
        
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False
        
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))


# ### Test Code
# 
# Here we create a new Graph object. We create a new vertex named A, We add A to the graph. The we add new vertex B to the graph. Then we iterate from A to K and a bunch of vertices to the graph. Since the add_vertex method checks for duplicates, A and B are not added twice

# In[3]:


graph = Graph()
a = Vertex('A')
graph.add_vertex(a)
graph.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    graph.add_vertex(Vertex(chr(i)))
    


# An edge consist of two vertex names. Here we iterate through a list of edges and each to the graph  
#   
# This print_graph method does not give very good visualizatio of the graph but it does show  
# the neighbors for each vertex

# In[4]:


edges = ['AB', 'AE', 'BF', 'CG', 'DH', 'EH', 'FI', 'FJ', 'GJ', 'IJ', 'GH', 'IG']
for edge in edges:
    graph.add_edge(edge[0], edge[1])
    

graph.print_graph()


# ### Graph Implementation Using Adjaceny Matrix
# for an undirected graph with weighted or unweighted edges

# ### Vertex Class
# 
# A vertex object only needs to store its name

# In[5]:


class Vertex:
    
    def __init__(self, n):
        self.name = n


# ### Graph Class
# A graph object has three attributes
# 
# **vertices** - a dictionary with vertex_name:vertex_object  
# **edges**  - a 2-d list (i.e a matrix) of edges for an unweightes graph it will contain 0 for no edge and 1   
# for edge.  
# **edge_indices** a dictionary with vertex_name: list_index (e.g A:O) to access edges  
# add_vertex updates all three of these attributes  
# add_edge only needs to update the edges matrix

# In[14]:


class Graph:
    
    vertices = dict()
    edges = list()
    edge_indices = dict()
    
    def __init__(self):
        pass
    
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges: # forloop append a column of zeros to the edges matrix
                row.append(0)
            # append a row of zeros to the bottom of the edges matrix
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False
        
    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False
        
    
    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v, ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print(' ')
            


# ### Test Code
# 
# Here we create a new Graph Object, We create a new vertex named A, We add A to the graph. Then we add a new  
# vertex B to the graph. The we iterate from A to K and add a bunch id vertices to the graph. Since the add_vertex method checks for duplication. A and B are not added twice. This is exactly the same test code for the graph with adjaceny list

# In[15]:


graph = Graph()
a = Vertex('A')
graph.add_vertex(a)
graph.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    graph.add_vertex(Vertex(chr(i)))


# In[16]:


edges = ['AB', 'AE', 'BF', 'CG', 'DH', 'EH', 'FI', 'FJ', 'GJ', 'IJ', 'GH', 'IG']
for edge in edges:
    graph.add_edge(edge[0], edge[1])
    

graph.print_graph()

