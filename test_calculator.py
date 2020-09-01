#Exercise 1
#importing libraries
import math
import pytest
#importing function
from calculator import add, factorial, sin, divide, exalted, subtract

#Test functions
def test_add():
    assert add(1,2) == 3, 'Function is not equal to 3'

def test_add_float():
    assert abs(add(0.1,0.2) - 0.3) < 1E-9, 'Function is not equal to 0.3'

def test_add_string():
    assert add('hello ','world') == 'hello world', 'Function does not compute "hello world"'

def test_factorial():
    n = 5
    assert abs(factorial(n) - math.factorial(n)) < 1E-9, 'Computed factorial is not equal to maths factorial'

def test_sin():
    x = 3; N = 10
    assert abs(sin(x,N)- math.sin(x)) < 1E-9, 'Computed sine is not equal to maths sine'

def test_divide():
    x = 5; y=15
    assert(abs(divide(x,y)-(x/y))) < 1E-9, 'Division is not equal to expected value'

def test_exalted():
    x = 2; n = 4
    assert abs(exalted(x,n) - (x**n)) < 1E-9, '%.f to the power of %.f is not equal the expected value' %(x,n)

def test_subtract():
    x = 3; y=7
    assert abs(subtract(x,y)-(x-y)) < 1E-9, 'Subtraction is not equal the expected value'

#Test function which raises TypeError on the add function
def test_add_type_error():
    x = 0.3; y='hello'
    with pytest.raises(TypeError):
        add(x,y)

#Test function which raises ZeroDivisionError on the divide function
def test_divide_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        divide(x=3,y=0)

#Parametrized test function for factorial
@pytest.mark.parametrize('n,expected',[(1,1),(4,24),(5,120)])
def test_factorial_parametrize(n,expected):
    assert factorial(n) == expected

#Parametrized test function for sin
@pytest.mark.parametrize('x,expected',[[(0.5,10),math.sin(0.5)],[(2,20),math.sin(2)], [(1,10),math.sin(1)]])
def test_sin_parametrize(x, expected):
    assert abs(sin(x[0],x[1]) - expected) < 1E-20

#Parametrizes test function for divide
@pytest.mark.parametrize('x,expected',[[(1,2),0.5],[(4,4),1],[(6,2),3]])
def test_divide_parametrize(x,expected):
    assert divide(x[0],x[1]) == expected

#Parametrized test function for exalted
@pytest.mark.parametrize('x,expected',[[(math.exp(1),0),1],[(2,3),8],[(9,2),81]])
def test_exalted_parametrize(x,expected):
    assert abs(exalted(x[0],x[1])-expected)<1E-17

#Parametrized test function for subtract
@pytest.mark.parametrize('x,expected',[[(1,1),0],[(3,2),1],[(29,3),26]])
def test_subtract_parametrize(x,expected):
    assert abs(subtract(x[0],x[1])-expected) < 1E-14

#Parametrized test function for add with respect to integers
@pytest.mark.parametrize('x, expected',[[(1,2),3],[(3,4),7],[(2,9),11]])
def test_add_parametrize(x,expected):
    assert abs(add(x[0],x[1])-expected) < 1E-14

#Parametrized test function for add with respect to floats
@pytest.mark.parametrize('x,expected',[[(0.3,0.3),0.6],[(0.2,0.1),0.3],[(0.1,0.1),0.2]])
def test_add_float_parametrize(x,expected):
    assert abs(add(x[0],x[1])-expected) < 1e-14

#Parametrized test function for add with respect to strings
@pytest.mark.parametrize('x,expected',[[('hello ','Henrik'), 'hello Henrik'], [('I am ', 'smart'), 'I am smart'], [('Geophysics is ', 'fun'), 'Geophysics is fun']])
def test_add_string_parametrize(x,expected):
    assert add(x[0],x[1]) == expected
