
## Quick Sort
Quick sort is a sorting algorithm that uses the divide-and-conquer strategy to sort the list of elements. The basic idea of quick sort is to partition the input list into two sub-list, one containing elements that are smaller than a chosen pivot element, and the other containing elements that are greater than or equal to the pivot. This process is repeated recursively on each sub-list until the entire list is sorted.

***Algorithm***
1. Choose a pivot element from the list. This can be any element, but typically the first or last element is chosen.

2. Partition the list into two sub-list, one containing elements smaller than the pivot, and the other containing elements greater than or equal to the pivot. Steps for Partition:-

    1. Set pivot to the value of the element at the lower index of the list L.

    1. Initialize two indices i and j to lower and lower+1 respectively.

    1. Loop over the range from lower+1 to upper (inclusive) using the variable j.

    1. If the value at index j is less than or equal to the pivot value, increment i and swap the values at indices i and j in the list L.

    1. After the loop, swap the pivot value at index lower with the value at index i in the list L.

    1. Return the index i as the position of the pivot value.

    1. Recursively apply steps 1 and 2 to each sub-list until the entire list is sorted.

***For Quick sort Code snippet click [here](/Chapter%203/quickSort.py)***

***Analysis***  
Recurrence relation - T(n)=2T(n/2)+O(n)   
Best Case - O(nlogn)  
Average Case  - O(nlogn)  
Worst Case - O(n<sup>2</sup>)  
Stable - No  
Sort in Place - Yes

![sorting algo comparision](/Chapter%203/image/sorting.png)

----------------------------------------------------------------

## Linked list
A linked list is a data structure consisting of a sequence of nodes, where each node contains a piece of data and a reference (or pointer) to the next node in the sequence. The first node is called the head, and the last node is called the tail, and the tail node points to null. Linked lists are useful for storing and manipulating collections of data, especially when the size of the collection is not known in advance, as they can dynamically adjust in size.  

There are mainly two types of linked lists:
- Singly Linked list
- Doubly Limked list

### Singly linked list
- `head` : Store the reference of the first node. If the list is empty, then it stores `none`.
- Each node has two fields:
    - data : Store actual value
    - next : Store the reference of the next node

***Representation***  
![singly linked list](/Chapter%203/image/sll.png)

### Doubly Linked list
- `head` : Store the reference of the first node. If the list is empty, then it stores `none`.
- `tail` : Store the reference of the last node. If the list is empty, then it stores `none`
- Each node have three fields : 
    - `prev` : store reference of the previous node
    - `data` : Store actual value
    - `next` : Store reference of the next node

***Representation***
![doubly linked list](/Chapter%203/image/dll.png)

***To see the implementation click [here](/Chapter%203/linkedlist.py)*** : using one class recursively  
***Using two classes [here](/Chapter%203/linkedListByTwoClass.py)***

***Advantage***  
- Insertion and deletion operations are easy
- Many Complex applications can be easily carried out with linked list concepts like tree ,graph etc.

***Disadvantages***
- More memory req to store data
- Random access is not possible  

***Applications***
- Implementation of stack,queue and deque
- Representation of graph 
- Representation of sparse matrix
- Manipulation of the polynomial expression

--------------------------------

## Stack
A Stack is a non-primitive linear data structure. It is an ordered list in which the addition of a new data item and deletion of an already existing data item can be done from only one end, known as top of the stack.

The last added element will be the first to be removed from the Stack. That is the reason why stack is also called Last In First Out (LIFO) type of data structure.

![stack](/Chapter%203/image/Stack.png)

### Basic operations on Stack
***Push***  

The process of adding a new element to the top of the Stack is called the `push` operation.  

***Pop***  

The process of deleting an existing element from the top of the Stack is called the `pop` operation. It returns the deleted value.  

***Traverse/Display***  

The process of accessing or reading each element from top to bottom in Stack is called the Traverse operation.  

### Applications of Stack
- Reverse the string
- Evaluate Expression
- Undo/Redo Operation
- Backtracking
- Depth First Search(DFS) in Graph

***Implementaion of the Stack is shown [here](/Chapter%203/stack.py)***  

***Implementation of the stack using linked list is shown [here](/Chapter%203/StackUsingLL.py)***

-----------------------------------------

## Queue
The Queue is a non-primitive linear data structure. It is an ordered collection of elements in which new elements are added at one end called the Back end, and the existing element is deleted from the other end called the Front end.

A Queue is logically called a First In First Out (FIFO) type of data structure.

![queue](/Chapter%203/image/queue.png)

### Basic operations on Queue
***Enqueue***  

The process of adding a new element at the `Back` end of Queue is called the `Enqueue` operation.  

***Dequeue***  

The process of deleting an existing element from the `Front` of the Queue is called the `Dequeue` operation. It returns the deleted value.

***Traverse/Display***  

The process of accessing or reading each element from `Front` to `Back` of the Queue is called the `Traverse` operation.

### Applications Of Queue
- Spooling in printers
- Job Scheduling in OS
- Waithing list application
- Breath First Search(BFS) in Graph

***Implementaion of Queue using list is [here](/Chapter%203/queueByList.py)***  
***Implementaion of Queue using linked list is [here](/Chapter%203/queueByLinkedList.py)***  

****************************************************************

## Hash mapping
Hash mapping, also known as hash table or dictionary, is a data structure that allows for efficient insertion, deletion, and retrieval of key-value pairs.

The basic idea behind hash mapping is to use a hash function to map the key to a bucket in an array. The hash function takes the key as input and returns an index of the array where the value corresponding to the key can be stored. When we want to retrieve a value, we simply use the hash function to calculate the index and then access the value stored at that index.

One of the advantages of hash mapping is its constant-time complexity for basic operations such as insertion, deletion, and retrieval, on average, making it efficient for large datasets. However, the performance can be affected by factors such as the quality of the hash function, the number of collisions (i.e., when multiple keys map to the same index), and the size of the array.

![hash](/Chapter%203/image/Hashing.png)

***Colision***  

The situation where a newly inserted key maps to an already occupied slot in the hash table is called collision.  

### Collision resolution technique
#### Open addressing(Close hashing)
- ***Linear probing*** is an open addressing scheme in computer programming for resolving hash collisions in hash tables. Linear probing operates by taking the original hash index and adding successive values linearly until a free slot is found.

   An example sequence of linear probing is:  
   `h(k)+0, h(k)+1, h(k)+2, h(k)+3 .... h(k)+m-1`
   where m is the size of hash table, and h(k) is the hash function.
***Hash Function***  

Let h(k) = k mod m be a hash function that maps an element k to an integer in [0, m−1], where m is the size of the table. Let the  ith probe position for a value k be given by the function

h'(k,i) = (h(k) + i) mod m 

The value of i = 0, 1, . . ., m – 1. So we start from i = 0, and increase this until we get a free block in hash table.

- ***Quadratic probing*** is an open addressing scheme in computer programming for resolving hash collisions in hash tables. Quadratic probing operates by taking the original hash index and adding successive values of an arbitrary quadratic polynomial until an open or empty slot is found.

  An example of a sequence using quadratic probing is: h,h+1,h+4,h+9...h+i<sup>2</sup>

***Quadratic function***  

Let h(k) = k mod m be a hash function that maps an element k to an integer in [0, m−1], where m is the size of the table. Let the  
 probe position for a value k be given by the function

where c1 and c2 are positive integers. The value of i = 0, 1, . . ., m – 1. So we start from i = 0, and increase this until we get one free slot in hash table.

#### Closed addressing ( Open hashing)
- ***Separate chaining using linked list*** : Maintain the separate linked list for each possible generated index by the hash function.

  For example, if the hash function is k mod 10 where k is the key and 10 is the size of the hash table.  

  ![open hashing](/Chapter%203/image/OpenHashing.png)


### End of this Chapter :)
Go to the [next Chapter](/Chapter_4.md)