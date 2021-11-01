def fibonacci(n):
    
    """
    The function should return the nth value in the fibonacci series. The series will start from 0,1 and start adding the previous two number determing the next number.
    """
    if n<0:
        return('No negative numbers allowed')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) 


def lucas(n):
    """
    Returns the nth value in the lucas numbers series. The series will start from 
    """
    if n<0:
        return('Negative numbers not allowed')
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


def sum_series(a,b,num):
    if num<0:
        return("wrong value")
    elif num == 0:
        return a
    elif num == 1:
        return b
    else:
        return sum_series(a,b,num-1)+sum_series(a,b,num-2)


