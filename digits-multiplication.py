def checkio(number):
    num = 1
    for n in range(len(str(number))):
        if not str(number)[n] == '0':
            num*=int(str(number)[n])
    return num

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print( checkio(123405))# == 120
    print( checkio(999))# == 729
    print( checkio(1000) )#== 1
    print( checkio(1111) )#== 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
