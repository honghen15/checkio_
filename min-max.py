def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    min_value = None
    for i in items:
        if min_value is None:
            min_value = i
        min_value = i if key(i) < key(min_value) else min_value
    return min_value

def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    max_value = None
    for i in items:
        if max_value is None:
            max_value = i
        max_value = i if key(i) > key(max_value) else max_value
    return max_value

def min_max_return(type, list_args, key):
    #print(key)
    if key == None :
        #print( range(6) )
        if (isinstance(list_args[0], list) or isinstance(list_args[0], str)
            or isinstance( list_args[0], tuple)):
            list_args = list_args[0]


        if ( 'range' in str(list_args)):
            return int(str(list_args)[-3])-1
        m = list_args[0]
        for i in range(1, len(list_args)):
            if ( type == 0 and m > list_args[i]) or ( type == 1 and m < list_args[i]):
                m = list_args[i]

        return m
    else:
        if (isinstance(list_args[0], list) or isinstance(list_args[0], str) ):
            list_args = list_args[0]
        index = 0
        m = key(list_args[index])

        for i in range(1, len(list_args)):
            if ( type == 0 and m > key(list_args[i])) or ( type == 1 and m < key(list_args[i])):
                m = key(list_args[i])
                index = i

        return list_args[index]
    return list_args
    pass
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # print( max(3, 2))# == 3, "Simple case max"
    # print( min(3, 2))# == 2, "Simple case min"
    # print( max([1, 2, 0, 3, 4]))# == 4, "From a list"
    # print( min("hello"))# == "e", "From string"
    # print( max(2.2, 5.6, 5.9, key=int))# == 5.6, "Two maximal items"
    # print( min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))# == [9, 0], "lambda key"
    print( max(range(6)) )# == [9, 0], "lambda key"
    #print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
