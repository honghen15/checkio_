def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if (len(array)<=n):
        return -1
    elif n == 0:
        return 1
    else:
        return array[n]**n
    return None
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( index_power([1, 2, 3, 4], 2))# == 9, "Square"
    print(index_power([1, 3, 10, 100], 3))# == 1000000, "Cube"
    print(index_power([0, 1], 0))# == 1, "Zero power"
    print(index_power([1, 2], 3))# == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
