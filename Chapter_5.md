## Weighted directed graph

#### Adjacency matrix representation in python

```python
# Each tuple (u,v,d) in list is representing the edge from u to v with weight d
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,w) in dedges:
    W[i,j,0] = 1
    W[i,j,1] = w
print(W)
```

### Adjacency list representation in Python

```python
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in dedges:
    WL[i].append((j,d))
print(WL)
```

## Weighted undirected graph

### Adjacency matrix representation in python

```python
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
# Each edge represented by two entry in data structure ((u,v,d) and (v,u,d) for undirected graph
edges = dedges + [(j,i,w) for (i,j,w) in dedges]
size = 7
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,w) in edges:
    W[i,j,0] = 1
    W[i,j,1] = w
print(W)
```

### Adjacency list representation in the Python

```python
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
edges = dedges + [(j,i,w) for (i,j,w) in dedges]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edges:
    WL[i].append((j,d))
print(WL)
```


# Shortest path 

## Single source shortest path algorithm
Find shortest paths from a source vetex to every other vertex.
- Dijkstra algorithm
- Bellman ford algorithm

### Dijkstra algorithm
***Dijkstra's algorithm is a popular algorithm for finding the shortest path between two vertices in a weighted graph. Some of its important properties and points are:

1. ***Single-source shortest path:*** Dijkstra's algorithm finds the shortest path from a single source vertex to all other vertices in the graph.

1. ***Weighted graph:*** Dijkstra's algorithm only works on weighted graphs, where each edge has a weight or cost associated with it.

1. ***Non-negative weights:*** Dijkstra's algorithm can only be used on graphs with non-negative edge weights. If the graph contains negative weights, Bellman-Ford algorithm is a better choice.

1. ***Greedy algorithm:*** Dijkstra's algorithm is a greedy algorithm that selects the vertex with the smallest distance from the starting vertex and explores its neighbors. This process is repeated until the shortest path to all vertices is found.

1. ***Optimal substructure:*** Dijkstra's algorithm relies on the optimal substructure property, which means that the optimal solution to a problem can be obtained by combining the optimal solutions to its subproblems.

1. ***Can handle disconnected graphs:*** Dijkstra's algorithm can handle disconnected graphs, but it will only find the shortest path for the connected component containing the source vertex.

#### Algorithm steps
***Here is the steps for Dijkstra algorithm for finding the single source shortest path:***  

1. Create a table to store the distances from the source vertex to each vertex in the graph. Initialize the source vertex with a distance of 0 and all other vertices with infinity. Also create a set of unvisited vertices and mark all vertices as unvisited.

1. While the set of unvisited vertices is not empty, do the following:

1. Select the unvisited vertex with the smallest distance from the source vertex. This vertex is now considered visited.

1. For each neighbor of the visited vertex that is still unvisited, calculate the distance to that neighbor by adding the weight of the edge between the visited vertex and the neighbor to the distance of the visited vertex. If this distance is smaller than the distance currently stored for the neighbor in the table, update the table with the new distance.

1. After updating the distances for all neighbors, mark the visited vertex as visited.

1. Repeat steps 3 to 5 until all vertices have been visited or the destination vertex has been visited.

1. Once the algorithm has visited all vertices, the table will contain the shortest distances from the source vertex to each vertex in the graph.

1. To find the shortest path from the source vertex to a destination vertex, backtrack from the destination vertex to the source vertex by following the path with the smallest distance at each step. This will give you the shortest path from the source vertex to the destination vertex.

***Implementation of Dijkstra's algorithm for adjacency matrix is given [here](/Chapter%205/Dijkstra_AlgorithmsMatrix.py)***

***Complexity : O(V^2)***

***Implementation of Dijkstra's algorithm for ajacency list is given [here](/Chapter%205/Dijkstra_algorithms_list.py)***

***Complexity : O(V^2)***


###  Bellman Ford algorithm
Bellman-Ford algorithm is a dynamic programming based algorithm to find the shortest path in a weighted graph, where the edge weights may be negative. Here are some important points and properties of the algorithm:

1. ***It can handle graphs with negative edge weights:*** Unlike Dijkstra's algorithm, which can only handle non-negative edge weights, the Bellman-Ford algorithm can handle graphs with negative edge weights. However, it cannot handle graphs with negative cycles, which are cycles that have a negative sum of edge weights.

1. ***It can detect negative cycles:*** The Bellman-Ford algorithm can detect negative cycles in a graph. If there is a negative cycle, the algorithm will report that there is no shortest path from the source vertex to some other vertex.

1. ***It can handle disconnected graphs:*** The Bellman-Ford algorithm can handle disconnected graphs by finding the shortest paths from the source vertex to all other vertices in each connected component.

1. ***It uses dynamic programming:*** The Bellman-Ford algorithm uses dynamic programming to solve the shortest path problem. It maintains an array of distances that is gradually updated until it converges to the correct values.

1. Bellman-Ford works for both directed and undirected graphs with non-negative edges weights.

#### Algorithm steps
Here are the step-by-step instructions for the Bellman-Ford algorithm:

1. ***Initialize the distance array:*** Set the distance of the source vertex to 0 and the distances of all other vertices to infinity.

1. ***Relax all edges:*** Repeat the following step (V-1) times, where V is the number of vertices in the graph. For each edge (u,v) with weight w, if the distance to u plus w is less than the distance to v, update the distance to v to the distance to u plus w.

1. ***Check for negative weight cycles:*** After relaxing all edges V-1 times, check for negative weight cycles. For each edge (u,v) with weight w, if the distance to u plus w is less than the distance to v, there exists a negative weight cycle.

1. ***Print the distance array:*** If there are no negative weight cycles, print the distance array, which contains the shortest path distances from the source vertex to all other vertices.

***Imlementaion of Bellman Ford for ajdacency matrix is shown [here](/Chapter%205/BellmanMatrix.py).***

***Complexity : O(v^2) where V is the number of vertices.***  

***Imlementaion of Bellman Ford for ajdacency matrix is shown [here](/Chapter%205/BellmanList.py).***  

***Complexity : O(v * E) where V is the number of vertices and E is number of edges.***  


### Floyd-Warshall algorithm
The Floyd-Warshall algorithm is an efficient algorithm for finding the shortest path between all pairs of nodes in a weighted graph. Some important points and properties of the Floyd-Warshall algorithm are:

1. ***All-pairs shortest path:*** The Floyd-Warshall algorithm computes the shortest path between all pairs of nodes in the graph.

1. ***Negative cycles:*** The Floyd-Warshall algorithm can detect negative cycles in the graph. A negative cycle is a cycle in the graph where the sum of the weights of the edges is negative. If there is a negative cycle in the graph, then the algorithm will report that there is a negative cycle.

1. ***Dynamic programming:*** The Floyd-Warshall algorithm uses dynamic programming to compute the shortest path between all pairs of nodes in the graph. The algorithm builds a table of shortest paths between pairs of nodes by iteratively considering intermediate nodes along the path.

1. ***No guarantee of uniqueness:*** The shortest path between two nodes in a graph may not be unique. If there are multiple shortest paths between two nodes, then the Floyd-Warshall algorithm may return any one of them.

1. Floyd-Warshall's works for both directed and undirected graphs with non-negative edges weights.

1. Floyd-Warshall's does not work with an undirected graph with negative edges weight, as it will be declared as a negative weight cycle.

#### Algorithms steps

1. Initialization: Create a 2-dimensional array SP of size n x n, where n is the number of vertices in the graph. For each pair of vertices (i,j), initialize SP[i][j] to the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, then set SP[i][j] to infinity.

1. For each vertex k from 1 to n, compute the shortest path between every pair of vertices (i,j) that passes through k. To do this, update SP[i][j] as follows:
SP[i][j] = min(SP[i][j], SP[i][k] + SP[k][j])

1. This means that the shortest path from vertex i to vertex j that passes through k is the minimum of the current shortest path from i to j and the sum of the shortest path from i to k and the shortest path from k to j.

1. After the step 2 is complete, the SP array will contain the shortest path between every pair of vertices in the graph.

***Implementation of Floyd Warshall's Algorithms is shown [here](/Chapter%205/FloydWarshall.py).***  


***Complexity : O(v^3) where V is the number of vertices in the graph.***

********

## Spanning Tree(ST)
- Retain a minimal set of edges so that graph remains connected 

- Recall that a minimally connected graph is a tree 

- Adding an edge to a tree creates a loop 

- Removing an edge disconnects the graph 

- Want a tree that connects all the vertices — **spanning tree** 

- More than one spanning tree, in general

### Minimum Cost Spanning Tree(MCST)
- Add the cost of all the edges in the tree 

- Among the different spanning trees, choose one with minimum cost

- Some facts about trees

  - A tree on n vertices has exactly n − 1 edges

  - Adding an edge to a tree must create a cycle.

  - In a tree, every pair of vertices is connected by a unique path

#### Algorithm
- Prim's Algorithm
- Kruskal's Algorithm

### Prim's Algorithm
Prim's algorithm is a greedy algorithm that finds a minimum spanning tree (MST) for a weighted undirected graph. Here are some of the key points or properties of Prim's algorithm:

1. **Greedy approach:** Prim's algorithm is a greedy algorithm that works by building up the MST one vertex at a time, always choosing the cheapest edge that connects the growing tree to an outside vertex.

1. **Works on connected graphs:** Prim's algorithm only works on connected graphs, meaning that there must be a path between any two vertices in the graph.

1. **Weighted edges:** Prim's algorithm requires that the graph have weighted edges. The weights represent the cost or distance of traveling between two vertices.

1. **Spanning tree:** Prim's algorithm always produces a spanning tree, which is a subset of the edges that connects all vertices in the graph and contains no cycles.

1. **Unique solution:** If the weights of the edges are unique, then the MST produced by Prim's algorithm is unique.  

#### Algorithm steps 

1. Choose any vertex as the starting vertex and add it to the MST set. Initialize the weight of this vertex to 0.

1. Find the edge with the minimum weight that connects the starting vertex to any other vertex.

1. Add the adjacent vertex connected by the minimum weight edge to the MST set. Set its weight to the weight of the edge.

1. Repeat steps 2 and 3 until all vertices are included in the MST set.  

**Implementation of Prim's Algorithm is given [here](/Chapter%205/prims.py) and [here](/Chapter%205/primsList.py).**

**Complexity : O(V^2) Where V is the number of vertices.**

### Kruskal's Algorithm
Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a connected, undirected graph. The algorithm works by iteratively adding the edges of the graph with the smallest weights that do not create a cycle in the MST. Here are some important points and properties of Kruskal's algorithm:

1. Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a connected, undirected graph.

1. The algorithm works by iteratively adding the edges of the graph with the smallest weights that do not create a cycle in the MST.

1. Kruskal's algorithm guarantees that the MST is unique if the graph has unique edge weights.

#### Algorithm steps
**Here are the steps for the of Kruskal's algorithm:**

1. Sort all the edges of the graph in non-decreasing order of their weights.

1. Create a new empty set for the minimum spanning tree (MST).

1. Iterate through the sorted edges, starting with the edge with the smallest weight.

1. For each edge, check if adding it to the MST will create a cycle. 

1. If the edge does not create a cycle, add it to the MST.

1. Repeat steps 4 and 5 until all vertices are included in the MST, or until the desired number of edges have been added.

1. Return the MST.1. 

**Implementation of Kruskal's algorithm is given [here](/Chapter%205/Kruskal.py).**

**Complexity : O(V^2) where V is the number of vertices.**