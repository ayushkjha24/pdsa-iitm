***_This documentation will cover the concepts like finding gcd ,gcd by eulid's algorithm , finding primes , exception handling , classes and objects , Timer class and setting of recursion limit._***

# Computing gcd
### 1st approach
```python
def gcd(m,n):
  (a,b) = (max(m,n),min(m,n))
  if a%b == 0:
    return b
  else
    return (gcd(b,a-b))
```

### Computing gcd - Euclid's algorithm

```python
def gcd(m,n):
  (a,b) = (max(m,n),min(m,n))
  if a%b == 0:
    return b
  else
    return (gcd(b,a%b))
```
***
## Computing primes
***Diretctly check if n has a factor between 2 and n-1***

```python
def prime(n):
  result = True
  for i in range(2,n):
    if(n % i) == 0:
      result = false
  return result
```

***Directly check if n hac a factor between 2 and n//2***
```python
def prime(n):
    result = True
    for i in range(2,n//2):
        if (n%i) == 0:
            result = False
    return(result)
```

***Computing primes sufficient to check factors up to squareroot(n)***
```python
import math
def prime(n):
    (result,i) = (True,2)
    while (result and (i <= math.sqrt(n))):
        if (n%i) == 0:
            result = False
        i = i+1
    return(result)
```

----

## Exception Handling

***Our code could generate many types of errors***

- y = x/z, but z has value 0 
- y = int(s), but string s does not - represent a valid integer 
- y = 5*x, but x does not have a value 
- y = l[i], but i is not a valid index for list l 
- Try to read from a file, but the file does not exist 
- Try to write to a file, but the disk is full

***Types of some common errors***
- `SyntaxError : invalid syntax`
- Name used before value is defined - `NamedError : name 'x' is not defined`
- Division by zero in arithmetic expression - `ZeroDivisionError : division by zero`
- Invalid list index `IndexError : list assignment index out of range`

****Handling exceptions****
```python
try:
    #... ← Code where error may occur
except (IndexError):
    #... ← Handle IndexError 
except (NameError,KeyError):
    #... ← Handle multiple exception types 
except:
    #... ← Handle all other exceptions 
else:
    #... ← Execute if try runs without errors
```
----
***Example on class and object***
```python
class Point:
  def __init__(self,a=0,b=0):
    self.x = a
    self.y = b

  def translate(self,deltax,deltay):
    self.x += deltax
    self.y += deltay

  def odistance(self):
    import math
    d = math.sqrt(self.x*self.x +
                  self.y*self.y)
    return(d)

  def __str__(self):
    return('('+str(self.x)+','
            +str(self.y)+')')

  def __add__(self,p):
    return(Point(self.x + p.x, 
                 self.y + p.y))

p = Point(3,4)
q = Point(5,8)
print(p)
print(p+q)
```
----
### Incorporating Timer class in Python

```python
import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None:
           raise TimerError("Timer is not running. Use .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed_time is None:
           raise TimerError("Timer has not been run yet. Use .start()")
        return(self_elapsed_time)

    def __str__(self):
        """print() prints elapsed time"""
        return(str(self._elapsed_time))
```

### Set recursion limit for performing large operations

```python
import sys
sys.setrecursionlimit(10000000)
gcd(2,99999)
```

## End of this chapter, Congratulations for reading this section till the end :)
Go to the [next Chapter](/Chapter_2.md)