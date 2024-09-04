## Divide and Conquer
- Break up a problem into disjoint subproblems 
- Combine these subproblem solutions efficiently 
- **Examples** 

    - Merge sort 
        - Split into left and right half and sort each half separately 
        - Merge the sorted halves
    - Quicksort 
        - Rearrange into lower and upper partitions, sort each partition separately 
        - Place pivot between sorted lower and upper partitions

## Divide and Conquer example
### Counting inversions
- Compare your profile with other customers 
- Identify people who share your likes and dislikes 
- No inversions – rankings identical 
- Every pair inverted – maximally dissimilar 
- Number of inversions ranges from 0 to n(n – 1) / 2 
- An inversion is a pair (i, j), i < j, where j appears before i 
- Recurrence: T(n)=2T(n/2)+n = O(nlogn)

**Implementation of counting inversions is [here](/Chapter%208/counting_inversions.py).** 

### Closest pair of points
- Several objects on screen 
- Basic step: find closest pair of objects 
-  objects — naive algorithm is 
    - For each pair of objects, compute their distance 
    - Report minimum distance across all pairs 
- There is a clever algorithm that takes time O(nlogn) using divide and conquer
- Given n points p1,p2,....,pn find the closest pair 
    - Assume no two points have same x or y coordinate
    - Split the points into two halves by vertical line 
    - Recursively compute closest pair in each half 
    - Compare shortest distance in each half to shortest distance across the dividing line 
- Recurrence: T(n)=2T(n/2) + O(n)
- Overall: O(nlogn)

**Pseudocode**
```python
def ClosestPair(Px,Py):
    if len(Px) <= 3:
        compute pairwise distances
        return closest pair and distance
    Construct (Qx,Qy), (Rx,Ry)
    (q1,q2,dQ) = ClosestPair(Qx,Qy)
    (r1,r2,dR) = ClosestPair(Rx,Ry)
    Construct Sy from Qy,Ry
    Scan Sy, find (s1,s2,dS)
    return (q1,q2,dQ), (r1,r2,QR), (s1,s2,dS)
    #depending on which of dQ, dR, dS is minimum
```

**Implementation of closest pair is [here](/Chapter%208/closest_pair.py).**

