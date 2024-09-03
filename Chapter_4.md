## Indroduction  to Graph
***Graph*** : It is a non-linear data structure. A graph G consist of a non empty set V where members are called the vertices of graph and the set E where member are called the edges.

G = (V, E)

V = set of vertices

E = set of edges

![graph]()

G = (V, E)

V = {A,B,C,D,E}

E = {e1,e2,e3,e4,e5} or {(A,B), (A,C), (B,C), (C,D), (C,E)}

### Basic terminology of Graph
***Vertex(or node):***  
A vertex or node is a fundamental unit in a graph. In a simple graph, each vertex can be connected to other vertices by edges. Vertices are often represented by circles or dots in visual representations of graphs.  
***Edge:***  
An edge is a line or connection between two vertices in a graph. Edges can be directed or undirected, and weighted or unweighted. In an undirected graph, edges connect vertices without a specified direction, while in a directed graph, edges have a direction, represented by an arrow. In a weighted graph, edges have a numerical weight or value assigned to them.  
***Degree:***
The degree of a vertex is the number of edges that are connected to it. In a directed graph, the degree of a vertex is defined as the sum of the in-degree (number of edges coming into the vertex) and out-degree (number of edges going out of the vertex).  
***Path :***  
A path is a sequence of vertices connected by edges. A simple path is a path where no vertex is repeated.  
***Cycle:***  
A cycle is a path that starts and ends at the same vertex.  

***Connectedness:*** 

A graph is said to be connected if there is a path between any two vertices in the graph. A disconnected graph is a graph that is not connected, meaning it can be broken into two or more separate components.

***Component:*** 

A component is a connected subgraph of a larger graph. In other words, it is a part of the graph that is connected to other vertices or edges within that part, but not connected to the rest of the graph.

***Directed graph:*** 

A directed graph is a graph where edges have a direction, represented by an arrow. In a directed graph, edges are often called arcs.

***Undirected graph:*** 

An undirected graph is a graph where edges do not have a direction.

***Weighted graph:*** 

A weighted graph is a graph where edges have weights or values assigned to them.

***Adjacent vertices:*** 

Two vertices are adjacent if they are connected by an edge.

***Incidence:*** 

A vertex is incident on an edge if the vertex is one of the endpoints of the edge.

***Subgraph:*** 

A subgraph is a graph that is a subset of another graph, with some edges and vertices removed.

***Complete graph:*** 

A complete graph is a graph where every vertex is connected to every other vertex. In other words, there is an edge between every pair of vertices in the graph.

### Logical representation of Graph
![graphs]()


### Graph representation in data structure

#### Adjacency matrix:
An adjacency matrix is a two-dimensional array or list that represents a graph. The matrix has a row and column for each vertex, and the value at position (i, j) indicates whether there is an edge between vertices i and j. If there is an edge, the value is 1, and if there is no edge, the value is 0. This representation is useful for dense graphs, where the number of edges is close to the maximum possible number of edges. In python we can use NumPy array or python list for adjacency matrix.  

#### Adjacency list:
An adjacency list is a list of lists where each vertex has a list of its adjacent vertices. Each list contains the vertices that are adjacent to the vertex at that index. This representation is useful for sparse graphs, where the number of edges is much smaller than the maximum possible number of edges. In python we can use dictionary for adjacency list.  

#### For unweighted directed graph

G = (V, E)

V = [0,1,2,3,4]

E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] 

#### Adjacency matrix representation:
***_Using NumPy 2d array_***
```python
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] # each tuple(u,v) represent edge from u to v
size = len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1 # mark 1 if edge present in graph from i to j , otherwise 0
print(AMat)
```
***Using python nested list***
```python
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
size = len(V)
AMat = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    AMat.append(row.copy())       
for (i,j) in E:
    AMat[i][j] = 1 # mark 1 if edge present in graph from i to j , otherwise 0
print(AMat)
```

#### Adjacency list representation

***_Using python dictionary_***
```python
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
size = len(V)
AList = {}
# In dictionay AList, for example, AList[i] = [j,k] represent two edge from i to j and i to k
for i in range(size):
    AList[i] = []
for (i,j) in E:
    AList[i].append(j)
print(AList)
```
### For unweighted undirected graph



## Graph Traveral algorithms
Graph traversal is the process of visiting all the vertices (nodes) of a graph. There are two commonly used algorithms for graph traversal:

1. Breadth-First Search (BFS)

2. Depth-First Search (DFS)

### Breadth First Search(BFS)
The Breadth First Search (BFS) algorithm is used to traverse a graph or a tree in a breadth-first manner. BFS starts at the root node and explores all the neighboring nodes at the current depth before moving on to the nodes at the next depth. This is done by using a queue data structure. The algorithm marks each visited node to avoid revisiting it.

### Algorithm
***Here are the steps for the BFS algorithm:***

1. Choose a starting node and enqueue it to a queue.

1. Mark the starting node as visited.

1. While the queue is not empty, dequeue a node from the front of the queue.

1. For each of the dequeued node's neighbors that are not visited, mark them as visited and enqueue them to the queue.

1. Repeat steps 3-4 until the queue is empty.

To keep track of the traversal order, you can add each visited node to a list as it is dequeued from the queue.

Complexity is O(V<sup>2</sup>) using adjacency matrix, O(V+E) using adjacency list, Where V is number of vertices and E is number of edges in Graph

For Codes visit [here](/Chapter%204/)
