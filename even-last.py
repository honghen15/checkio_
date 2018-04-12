def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    sum1 = sum( n for n in array[::2])
    multi = sum1*array[len(array)-1] if len(array)>0 else 0
    #print(multi)
    #sum for n in array[::2] sum+=n
    #print(sum1)
    return multi

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print( checkio([0, 1, 2, 3, 4, 5]))# == 30, "(0+2+4)*5=30"
    print( checkio([1, 3, 5]))# == 30, "(1+5)*5=30"
    print( checkio([6]))# == 36, "(6)*6=36"
    print( checkio([]))# == 0)#, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
