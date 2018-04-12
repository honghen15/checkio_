def checkio(numbers_array):
    dict_num = {}
    for num in numbers_array:
        dict_num[num if num>= 0 else num*-1] = num
        #print(dict_num.keys())
    list1 = []
    list2 = []
    # numbers_array1 = numbers_array
    for n in numbers_array:
        n = n*-1 if n<0 else n
        list1.append(n)
    list1 = sorted(list1)

    for n in list1:
        list2.append(dict_num[n])
    #print(numbers_array1)
    #list1 = []
    # for n in numbers_array1:
    #     print(dict_num[n])
    #     #list1.append(dict_num[n])
    #print(list2)
    return list2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    print( check_it(checkio((-20, -5, 10, 15))))# == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    print( check_it(checkio((1, 2, 3, 0))) )#== [0, 1, 2, 3], "Positive numbers"
    print( check_it(checkio((-1, -2, -3, 0))) )#== [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
