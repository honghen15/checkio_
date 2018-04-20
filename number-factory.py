def checkio(number):
    #replace this for solution
    duplicate = False
    listnum = []
    for i in range(9, 1, -1):
        num = i
        number1 = number
        strnum = ''
        while number1 != 1:
            if number1 % num != 0:
                num -= 1
                if num == 1 and number1 != 1:
                    break
            else:
                number1 /= num
                strnum += str(num)
            if number1 == 1:
                break
        if number1 == 1:
            listnum.append(int(strnum[::-1]))

    if not listnum:
        return 0
    else:
        return min(listnum)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(20))  # == 45, "1st example"
    print(checkio(21))  # == 37, "2nd example"
    print(checkio(17))  # == 0, "3rd example"
    print(checkio(33))  # == 0, "4th example"
    print(checkio(3125))  # == 55555, "5th example"
    print(checkio(9973))  # == 0, "6th example"
    print(checkio(81))  # == 99, "6th example"
    print(checkio(560))  # == 99, "6th example"
