"""
    Fibonacci series as list.

    Author: George Heineman
"""
def fibonacci(n):
    """Return first n>=2 elements of fibonacci as list."""
    a = b = 1
    result = [a, b]
    while n > 2:
        n = n - 1
        a,b = b,a+b       # 1+1 a=1 b=2; 1+2 a=2 b=3; 2+3 a=3 b=5; 3+5 a=5 b=8
        result.append(b)
    return result

def fibonacciGenerator(n):
    """Return first n>=2 elements of fibonacci as generator."""
    a = b = 1
    yield a
    yield b
    while n > 2:
        n = n - 1
        a,b = b,a+b
        yield b

        

"""
Sample Output:

>>> fibonacci(7)
[1, 1, 2, 3, 5, 8, 13]
>>> for _ in fibonacciGenerator(5):
	print (_)
	
1
1
2
3
5 

"""

