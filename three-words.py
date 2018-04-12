def checkio(words):
    lists = words.split(' ')
    # if (len(list1)<4 ):
    #     return False
    str1 = '123'
    str1.isdigit()
    count = 0
    for n in lists:
        if n.isdigit():
            count = 0
        else:
            count+=1
            if count == 3:
                break
    return True if count==3 else False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print( checkio("Hello World hello"))# == True, "Hello"
    print( checkio("He is 123 man") )#== False, "123 man"
    print( checkio("1 2 3 4"))# == False, "Digits"
    print( checkio("bla bla bla bla"))# == True, "Bla Bla"
    print( checkio("Hi"))# == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
