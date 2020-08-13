import time
n= int(input("digite un numero: "))
def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n<2:
        return 1
    else:
        return n*(get_recursive_factorial(n-1))

def get_interactive_factorial(n):
    if n<0:
        return -1
    else:
        a=1
        for i in range(1,n+1):
            n *= 1
        return n
        
start_time = time.time()
get_recursive_factorial(n)
print("Recursion---%s seconds---" % (time.time()-start_time))
start_time = time.time()
get_interactive_factorial(n)
print("Iteration--- %s seconds---" % (time.time()-start_time))