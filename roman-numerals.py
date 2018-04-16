roman_number = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,
                'D':500, 'M':1000}

def checkio(data):
    ret_data = ''
    flag = False
    sub_flag = False
    while data != 0:

        data, ret_data, flag, sub_flag = ret_data_func(data, 1000, 'M', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 900, 'CM', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 500, 'D', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 400, 'CD', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 100, 'C', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 90, 'XC', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 50, 'L', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 40, 'XL', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 10, 'X', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 9, 'IX', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 5, 'V', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 4, 'IV', ret_data, sub_flag)
        data, ret_data, flag, sub_flag = ret_data_func(data, 1, 'I', ret_data, sub_flag)
        sub_flag = False
    return ret_data

def ret_data_func(input_data, num, roman_letter, ret_data, sub_flag):
    if sub_flag == True:
        return input_data, ret_data, False, sub_flag
    if input_data >= num:
        input_data -= num
        ret_data += roman_letter
        sub_flag = True
        return input_data, ret_data, True, sub_flag
    sub_flag = False
    return input_data, ret_data, False, sub_flag
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(6))  # == 'VI', '6'
    print(checkio(76))  # == 'LXXVI', '76'
    print(checkio(499))  # == 'CDXCIX', '499'
    print(checkio(3888))  # == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
