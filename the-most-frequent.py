def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    dict_data = {}
    for n in data:
        if not ( n in dict_data):
            dict_data[n] = 1
        else:
            dict_data[n]+=1
    # your code here
    max_data = ['',-9999999999]
    for n in dict_data.keys():

        if max_data[1] < dict_data[n]:
            max_data[1] = dict_data[n]
            max_data[0] = n
        #print(max(dict_data[n]))
    #print(max_data)
    return max_data[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) )#== 'a'

    print( most_frequent(['a', 'a', 'bi', 'bi', 'bi'])) == 'bi'
    print('Done')
