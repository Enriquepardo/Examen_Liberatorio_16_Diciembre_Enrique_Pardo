from math import sqrt


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
        
def llamar_fibonacci():
    for i in range(2000000):
        print(fibonacci(i))       

    
