def checkio(data):
    return recursion_checkio(len(data), data)


def recursion_checkio(len_list, data):
    if len_list != 0:
        return data[len_list-1] + recursion_checkio(len_list-1, data)
    else:
        return 0


print(checkio([1, 2, 3]))
