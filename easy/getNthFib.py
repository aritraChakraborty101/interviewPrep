def getNthFib(n):
    result = 0
    first = 0
    second = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    while n - 2 > 0:
        result = first + second
        first = second
        second = result 
        n -= 1
    return result

#reccursive solution
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
