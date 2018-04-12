def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    count = 0
    max1 = 1
    if(line == ''):
        return 0
    letter = ''
    for i in line:
        if letter == '' or not (letter == i):
            letter = i
            count = 1
            if letter == '':
                max1 =1
        else:
            count+=1
            if ( max1 < count ):
                max1 = count

    return max1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( long_repeat('sdsffffse'))# == 4, "First"
    print( long_repeat('ddvvrwwwrggg'))# == 3, "Second"
    print( long_repeat('abababaab'))# == 2, "Third"
    print( long_repeat(''))# == 0, "Empty"
    print( long_repeat('abababa'))# == 1, "Empty"
    print('"Run" is good. How is "Check"?')
