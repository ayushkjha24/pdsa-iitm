## Balanced Search tree(AVL Tree)
#### Binary Search tree
- find(), insert() and delete() all walk down a single path
- Worst-case: height of the tree An unbalanced tree with n nodes may have height O(n)
  
#### AVL Tree
- Balanced trees have height O(logn)
- Using rotations, we can maintain height balance
- Height balanced trees have height O(logn)
- find(), insert() and delete() all walk down a single path, take time O(logn)
- Minimum number of node S(h)=S(h-2) + S(h-1) + 1
- Maximum number of nodes 2^h-1

**Implementation of AVL Tree is shown [here](/Chapter%207/avl.py).**


## Greedy Algorithm

- Need to make a sequence of choices to achieve a global optimum 

- At each stage, make the next choice based on some local criterion 

- Never go back and revise an earlier decision 

- Drastically reduces space to search for solutions 

- Greedy strategy needs a proof of optimality

- Example :

    - Dijkstra's
    - Prim's
    - Kruskal's
    - Interval scheduling
    - Minimize lateness
    - Huffman coding

### Interval scheduling 

**Scenario example**

▪ IIT Madras has a special video classroom for delivering online  lectures 

▪ Different teachers want to book the classroom 

▪ Slots may overlap, so not all bookings can be honored 

▪ Choose a subset of bookings to maximize the number of teachers  who get to use the room

**Algorithm**
1. Sort all jobs which based on end time in increasing order.
1. Take the interval which has earliest finish time.
1. Repeat next two steps till you process all jobs.
1. Eliminate all intervals which have start time less than selected interval’s end time.
1. If interval has start time greater than current interval’s end time, at it to set. Set current interval to new interval.

**Implementation of intervl scheduling is given [here](/Chapter%207/intervalScheduling.py).**  

**Analysis**
- Initially, sort n bookings by finish time - O(nlogn)
- Single scan , O(n)
- overall O(nlogn)

### Minimize lateness
**Scenario example:**  

▪ IIT Madras has a single 3D  printer   
▪ A number of users need to use  this printer   
▪ Each user will get access to the  printer, but may not finish before  deadline   
▪ Goal is to minimize the lateness 

**Algorithm**

1. Sort all job in ascending order of deadlines

1. Start with time t = 0

1. For each job in the list

    1. Schedule the job at time t
    1. Finish time = t + processing time of job
    1. t = finish time
1. Return (start time, finish time) for each job

**Implementation is shown [here](/Chapter%207/minimizeLateness.py).**  

**Analysis**

- Sort the requests by D(i) — O(nlogn)  
- Read all schedule in sorted order — O(n)  
- overall O(nlogn)


### Huffman Algorithm

**Algorithm**

1. Calculate the frequency of each character in the string.
1. Sort the characters in increasing order of the frequency.
1. Make each unique character as a leaf node.
1. Create an empty node z. Assign the minimum frequency to the left child of z and assign the second minimum frequency to the right child of z. Set the value of the z as the sum of the above two minimum frequencies.
1. Remove these two minimum frequencies from Q and add the sum into the list of frequencies.
1. Insert node z into the tree.
1. Repeat steps 3 to 5 for all the characters.
1. For each non-leaf node, assign 0 to the left edge and 1 to the right edge.

**Implementaions is [here](/Chapter%207/huffman.py).**  

**Huffman implementation using min heap is [here](/Chapter%207/huffmanMinHeap.py).**

**Analysis**
- At each recursive step, extract letters with minimum frequency and replace by composite letter with combined frequency 
- Store frequencies in an array  
- Linear scan to find minimum values 
- |A| = k, number of recursive calls is k-1
- Complexity is O(k^2)
- Instead, maintain frequencies in an heap 
- Extracting two minimum frequency letters and adding back compound  letter are both O(logk)
- Complexity drops to O(klogk)