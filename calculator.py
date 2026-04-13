"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError()
        return math.sqrt(a)
    except ValueError:
        raise
def hypotenuse(a,b):
    try:
        return math.hypot(a,b)
    except TypeError:
        raise TypeError()

def add(a, b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError()
    return b/a
def logarithm(a,b):
    if b <= 0 or a <= 1:
        raise ValueError()
    return math.log(b, a)
def exponent(a,b):
    return a**b
