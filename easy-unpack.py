def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    list1 = []
    # your code here
    list1.append(elements[0])
    list1.append(elements[2])
    list1.append(elements[len(elements)-2])
    return tuple(list1)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))# == (1, 3, 7)
    print( easy_unpack((1, 1, 1, 1)))# == (1, 1, 1)
    print( easy_unpack((6, 3, 7)))# == (6, 7, 3)
    print('Done! Go Check!')
