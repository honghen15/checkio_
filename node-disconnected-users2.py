import numpy as np

dictAlph = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7,
             'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15,
             'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23,
             'Y':24, 'Z':25}
def disconnected_users(net, users, source, crushes):

    np1 = np.zeros([len(users),len(users)])
    for pair in net:
        np1[dictAlph[pair[0]], dictAlph[pair[1]]] =1
        np1[dictAlph[pair[1]], dictAlph[pair[0]]] =1
    for i in crushes:
        np1[:, dictAlph[i]] = 0
        np1[dictAlph[i], :] = 0

    print(np1)
    list1 = [dictAlph[source]]
    for i in crushes:
        if dictAlph[i] in list1:
            list1.remove(dictAlph[i])
    nonzero = False
    for i in range(len(users)):
        for j in range(len(users)):
            if np1[i,j]==1:
                nonzero = True
                if not j in list1:
                    list1.append(j)
        if not nonzero:
            break
    print(list1)
    sum_num = sum(users.values())
    # print(list(dictAlph.keys()))
    # print(list(dictAlph.values()))
    #print(list(dictAlph.values()).index(list1[0]))
    #print(list(dictAlph.keys())[list(dictAlph.values()).index(list1[0])])
    for i in list1:
        num_alph = list(dictAlph.keys())[list(dictAlph.values()).index(i)]
        #print(users[num_alph])
        sum_num-=users[num_alph]
    return sum_num

def alph_to_num(net_list):
    net_copy = []
    for pair in net_list:
        pass

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']))# == 70, "First"

    print( disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']))# == 0, "Second"

    print( disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']))# == 50, "Third"

    print(disconnected_users([["A","B"],["B","C"],["C","D"]],{"A":10,"C":30,"B":20,"D":40},"A",["B"]))
    print('Done. Try to check now. There are a lot of other tests')
