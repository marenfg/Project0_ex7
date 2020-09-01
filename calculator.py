#Exercise 1
#importing libraries

#Functions
def add(x,y):
    return x+y

def factorial(n):
    factorial= 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial

def sin(x,N):
    sin = 0
    for n in range(N+1):
        sin += ((-1)**n*x**(2*n+1))/(factorial(2*n+1))
    return sin

def divide(x,y):
    return x/y

def exalted(x,n):
    return x**n

def subtract(x,y):
    return x-y
