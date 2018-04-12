import numpy as np

dictAlph = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7,
             'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15,
             'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23,
             'Y':24, 'Z':25}

def most_crucial(net, users):
    np1 = np.zeros([len(users),len(users)])
    for pair in net:
        np1[dictAlph[pair[0]], dictAlph[pair[1]]] =1
        np1[dictAlph[pair[1]], dictAlph[pair[0]]] =1
    #print(np1)
    #list1 = []
    # list1.append([3,4])
    # print(list1)
    #print(np.count_nonzero(np1, axis=1))
    min_value = [9999999999,-1]
    for i in range(len(users)):
        np1_tmp = np1.copy()
        raw_list1 = get_new_list(i, np1_tmp, len(users))
        print(raw_list1)
        cal_list1 = list_to_maxval(i, raw_list1, users)
        #print(cal_list1)
        #print(min_value[1], cal_list1)
        if min_value[0] > cal_list1:
            min_value[1] = i
            min_value[0] = cal_list1
        elif min_value[0] == cal_list1:
            min_value.append(i)
        #print(min_value)
        #print()
    if len(min_value)>0:
        list_ans =[]
        for ans in range(len(min_value)):
            if not ans == 0:
                list_ans.append(list(dictAlph.keys())[list(dictAlph.values()).index(min_value[ans])])
        return list_ans

def get_new_list(i, np1_tmp, len_user):
    list1 = []
    for ii in range(len_user):
        for jj in range(len_user):
            if ii <= jj:
                np1_tmp[ii,jj] = 0
    #print(np1_tmp)
    np1_tmp[:, i] = 0
    np1_tmp[i, :] = 0
    nonzero = False
    #print(np.count_nonzero(np1_tmp, axis=1), end=' ')
    for j in range(len_user):
        nonzero = False
        list1_tmp = []
        list1_tmp.append(j)
        for k in range(len_user):
            if j > k:
                exist_k_bool = False
                exist_k = 0
                if not np1_tmp[j, k] == 0:
                    for num in range(len(list1)):
                        if k in list1[num]:
                            list1_tmp = list1_tmp+list1[num]
                            exist_k = num
                            exist_k_bool = True
                            break
                    if exist_k_bool:
                        del list1[exist_k]
                    nonzero = True
            if j == k and not nonzero:
                break
        list1.append(list1_tmp)
    return list1

def list_to_maxval(i, list1, users):
    sum = 0
    for j in range(len(list1)):
        sub_sum = 0
        for num in list1[j]:
            n =list(dictAlph.keys())[list(dictAlph.values()).index(num)]
            # TODO 測試NUM可不可以換乘n

            sub_sum += users[n]

        sub_sum = sub_sum if i in list1[j] else sub_sum*sub_sum
        sum +=sub_sum
    #print(sum)
    return sum
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }))# == ['B'], 'First'

    print( most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }))# == ['A'], 'Second'

    print( most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }))# == ['A'], 'Third'

    print( most_crucial([["A","B"],["B","C"],["C","A"]],{"A":10,"C":10,"B":5}))# == ['B'], 'Forth'

    print(most_crucial([["A","B"],["B","C"],["B","D"],["C","E"],["D","E"],["E","F"]],{"A":10,"C":15,"B":20,"E":10,"D":15,"F":20}))
    print('Nobody expected that, but you did it! It is time to share it!')
