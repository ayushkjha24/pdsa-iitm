## Union-Find data structure
- A set S partitioned into components {C1, C2, . . . , Ck } 
    - Each s ∈ S belongs to exactly one Cj 
- Support the following operations 

    - MakeUnionFind(S) — set up initial singleton components {s}, for each s ∈ S 
    - Find(s) — return the component containing s 
    - Union(s,s’) — merges components containing s, s 0

**Naive implementation of union-find is [here](/Chapter%206/Union-Find.py).**

**Complexity**
- MakeUnionFind(S) - O(n)
- Find(i) - O(1)
- Union(i,j) - O(n)
- Sequence of m Union() operations takes time O(mn)


**Improved implementation of Union-Find is [here](/Chapter%206/Union-Find_improved.py).**

**Complexity**
- MakeUnionFind(S) - O(n)
- Find(i) - O(1)
- Union(i,j) - O(logn)


**Improved Kruskal's algorithm using Union-Find is [here](/Chapter%206/ImrovedKruskal.py).**


**Complexity**  
- Tree has n-1 edges, so O(n) Union() operations 
- O(nlogn) amortized cost, overall 
- Sorting E takes O(mlogm)
    - Equivalently O(mlogn), since m<=n^2
- Overall time, O((m+n)logn)


## Priority Queue
Need to maintain a collection of items with priorities to optimize the following operations
- delete max()
    - Identify and remove item with the highest priority
    - Need not be unique
- insert()
    - Add a new item to the list


## Heap 
### Binary tree
A binary tree is a tree data structure in which each node can contain at most 2 children, which are referred to as the left child and the right child.

#### Heap
Heap is a binary tree, filled level by level, left to right. There are two types of the heap:

- Max heap - For each node V in heap except for leaf nodes, the value of V should be greater or equal to its child's node value.
- Min heap - For each node V  in heap except for leaf nodes, the value of V should be less or equal to its child's node value.

**We can represent heap using array(list in python) :**  

H = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9]

left child of H[i] = H[2 * i + 1]  
Right child of H[i] =  H[2 * i + 2]  
Parent of H[i] = H[(i-1) // 2], for i > 0

**Implementation of max heap is shown [here](/Chapter%206/max_heap.py).**  

**Implementation of max heap is shown [here](/Chapter%206/min_heap.py).**

**Complexity:**
Heaps are a tree representation of priority queues
- insert() is O(logN)
- delete max() is O(logN)
- heapipy() builds a heap in O(N)

### Improve Dijkstra's  algorithm using min heap 
**Updated implementation for adjacency matrix using min heap is gven [here](/Chapter%206/Dijkstra_improved.py).**  

**Updated implementation for adjacency matrix using min heap is gven [here](/Chapter%206/Dijkstra_improved_list.py).**

***Complexity***  
using min-heaps: 
- Identifying next vertex to visit is 
- Updating distance takes 
 per neighbor 
- Adjacency list — proportionally to degree  

Cumulatively:-

-  O(nlogn) to identify vertices to visit across n iterations 
- O(mlogn) distance updates overall 
- Overall O((m+n)long)


### Heap Sort is [here](/Chapter%206/heapSort.py).

**Complexity**

- Start with an unordered list 
- Build a heap — O(n)
- Call delete max() n times to extract elements in descending order — O(nlogn)
- After each delete max(), heap shrinks by 1 
- Store maximum value at the end of current heap 
- In place O(nlogn) sort

## Binary Search Tree(BST)
**For dynamic stored data**
- Sorting is useful for efficient searching 
- What if the data is changing dynamically? 
- Items are periodically inserted and deleted Insert/delete in a sorted list takes time O(n)

**How can we improve Insert/delete time? - using tree structure?**

A binary search tree is a binary tree that is either empty or satisfies the following conditions:

For each node V in the Tree  
- The value of the left child or left subtree is always less than the value of V.
- The value of the right child or right subtree is always greater than the value of V.

**BST implementation is [here](/Chapter%206/bst.py).**

**Complexity**

- find(), insert() and delete() all walk down a single path 
- Worst-case: height of the tree 
- An unbalanced tree with n nodes may have height O(n)
- Balanced trees have height O(logn)
- Will see how to keep a tree balanced to ensure all operations remain O(logn)