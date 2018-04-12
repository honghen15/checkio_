import numpy as np
dictAlph = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7,
             'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15,
             'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23,
             'Y':24, 'Z':25}
def subnetworks(net, crushes):

    list_array = []
    max_num = 0
    for pair in net:
        print( pair[0], pair[1], end=' ')
        print( dictAlph[pair[0]], dictAlph[pair[1]])
        if dictAlph[pair[0]] > max_num:
            max_num = dictAlph[pair[0]]
        if dictAlph[pair[1]] > max_num:
            max_num = dictAlph[pair[1]]
        if not dictAlph[pair[0]] in list_array:
            list_array.append(dictAlph[pair[0]])
        if not dictAlph[pair[1]] in list_array:
            list_array.append(dictAlph[pair[1]])

    max_num+=1
    np1 = np.zeros([max_num, max_num])

    for pair in net:
        np1[dictAlph[pair[0]], dictAlph[pair[1]]] =1
        np1[dictAlph[pair[1]], dictAlph[pair[0]]] =1
    for i in crushes:
        np1[:, dictAlph[i]] = 0
        np1[dictAlph[i], :] = 0


    #print( len(list_array), max_num)
    #return np1
    count = 0
    for i in range(max_num):
        nonzero = False
        for j in range(max_num):
            if np1[i,j]==1:
                nonzero = True
                count+=1
        if not nonzero:
            count+=2
    count = count - (max_num-len(list_array))*2 -len(crushes)*2
    count /=2
    #print(np1)
    return int(count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']))# == 2, "First"
    print( subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']))# == 3, "Second"
    print( subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']))# == 1, "Third"
    print('Done! Check button is waiting for you!')
