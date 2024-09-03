## Dynamic programming
- Solution to original problem can be derived by combining solutions to subproblems   
***_Examples:_***  Factorial, Insertion sort, Fibonacci series 
- Anticipate the structure of subproblems 
- Derive from inductive definition
- Solve subproblems in topological order  

#### Memoization
- Inductive solution generates same subproblem at different stages 
- Naïve recursive implementation evaluates each instance of  subproblem from scratch 
- Build a table of values already computed – Memory table 
- Store each newly computed value in a table 
- Look up the table before making a recursive call  

***Example of n<sup>th</sup> number in Fibonacci series :***  
***_Simple recursive_***  
```python
def fibrec(n):
  if n <=1:
    return n
  return fibrec(n-1) + fibrec(n-2)
```
![fibonacci](/Chapter%209/image/fibonacciSimpleRecursive.png)
***_Memoization_***  
```python
memo ={}
def fib(n):
    if n <= 1:
        memo[n] = n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```
![memoization](/Chapter%209/image/memoization.png)

#### Dynamic programming
```python
def fib(n):
    T = [0] * (n + 1)
    T[1] = 1
    for i in range(2, n + 1):
        T[i] = T[i - 1] + T[i - 2]
    return T[n]
```
![dp](/Chapter%209/image/dp.png)

_For the comparision visit [here](/Chapter%209/compare.py)_  

