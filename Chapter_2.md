
## Complexity
The complexity of an algorithm is a function describing the efficiency of the algorithm in terms of the amount of input data. There are two main complexity measures of the efficiency of an algorithm:

#### Space Complexity
The space complexity of an algorithm is the amount of memory it needs to run to completion.

#### Time Complexity
The time complexity of an algorithm is the amount of computer time it needs to run to completion. Computer time represents the number of operations executed by the processor.

***Time Complexity calculated in three types of cases :***
- Best case (Omega)
- Average case (Theta)
- Worst case (Big-oh)

***Here are some common functions and their growth rates, listed from slowest-growing to fastest-growing:***
- constant time(1)
 - logarithmic time(logn)
 - linear time(n)
 - linearithmic time(nlogn)
 - quadratic time(n<sup>2</sup>)
 - cubic time(n<sup>3</sup>)
 - exponential time(2<sup>n</sup>)
 - factorial time(n!)


 ### Searching algorithms

 #### Linear Search or Naive Search
```python
def naivesearch(L,v):
  for i in range(len(L)):
    if v == L[i]:
      return i
  return(False)
```
***Analysis***

Best case = O(1)  
Avg case = O(n)  
Worst case = O(n)

#### Binary search (iterative implementation)
```python 
def binarysearch(L, v):  #v = target element
    low = 0
    high = len(L) - 1
    while low <= high: 
        mid = (low + high) // 2
        if L[mid ] < v:
            low = mid  + 1
        elif L[mid ] > v:
            high = mid  - 1
        else:
            return mid
    return False
```
#### Binary search recursive implementation without slicing
```python
def binarysearch(L,v,low,high): #v = target element, low = first index, high = last index
    if high - low < 0:
        return False
    mid = (high + low)//2
    if v == L[mid]:
        return mid
    if v < L[mid]:
        return(binarysearch(L,v,low,mid-1))
    else:
        return(binarysearch(L,v,mid+1,high))
```
### Binary search recursively but this approach is not recommended due to slicing because it can take O(n) time
```python
def binarysearch(L,v):
    if L == []:
        return(False)
    mid = len(L)//2
    if v == L[mid]:
        return mid
    if v < L[mid]:
        return(binarysearch(L[:mid],v))
    else:
        return(binarysearch(L[mid+1:],v))
```

***Analysis***
Best case = O(1)  
Avg case = O(logn)  
Worst case = O(logn)  

## Sorting Algorithm

### Selection Sort
```python

def selectionsort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if L[j] < L[minpos]:
                minpos = j
        (L[i],L[minpos]) = (L[minpos],L[i])
    return(L)
```

***Analysis***  
Best Case - O(n<sup>2</sup>)  
Average Case  - O(n<sup>2</sup>)  
Worst Case - O(n<sup>2</sup>)  
Stable - No  
Sort in Place - Yes


### Insertion Sort
```python
def insertionsort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        j = i
        while(j > 0 and L[j] < L[j-1]):
            (L[j],L[j-1]) = (L[j-1],L[j])
            j = j-1
    return(L)
```

***Analysis***  
Best Case - O(n)  
Average Case  - O(n<sup>2</sup>)  
Worst Case - O(n<sup>2</sup>)  
Stable - Yes  
Sort in Place - Yes


### Merge Sort
```python
def merge(A,B): # Merge two sorted list A and B
    (m,n) = (len(A),len(B))
    (C,i,j) = ([],0,0)
    
    #Case 1 :- When both lists A and B have elements for comparing
    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    #Case 2 :- If list B is over, shift all elements of A to C 
    while i < m:
        C.append(A[i])
        i += 1
    
    #Case 3 :- If list A is over, shift all elements of B to C 
    while j < n:
        C.append(B[j])
        j += 1
    
    # Return sorted merged list   
    return C



# Recursively divide the problem into sub-problems to sort the input list L    
def mergesort(L): 
    n = len(L)
    if n <= 1: #If the list contains only one element or is empty return the list.
        return(L)
    Left_Half = mergesort(L[:n//2]) #Recursively sort the left half of the list
    Right_Half = mergesort(L[n//2:]) #Recursively sort the rightt half of the list
    Sorted_Merged_List = merge(Left_Half, Right_Half) # Merge two sorted list Left_Half and Right_Half
    return(Sorted_Merged_List)
```
***Analysis***  
Recurrence relation - T(n)=2T(n/2)+O(n) 
Best Case - O(nlogn)  
Average Case  - O(nlogn)  
Worst Case - O(nlogn)  
Stable - Yes  
Sort in Place - No


## End ... Please read the Chapter 3 :)