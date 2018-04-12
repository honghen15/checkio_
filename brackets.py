def checkio(expression):
    bracket = {'()':0, '[]':0, '{}':0}
    for i in expression:
        #print(i, end='=>')
        if ( i == '(' ):
            print(1, i)
            bracket['()']+=1
        elif ( i == ')' ):
            print(2, i)
            bracket['()']-=1
        elif i == '[':
            print(3)
            bracket['[]']+=1
        elif i == ']':
            print(4)
            bracket['[]']-=1
        elif i == '{':
            print(5, i)
            bracket['{}']+=1
        elif i == '}':
            print(6)
            bracket['{}']-=1
    #print(bracket['()'])
    if (bracket['()']==0)and(bracket['[]']==0)and(bracket['{}']==0):
        return True
    return  False

    return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #print( checkio("((5+3)*2+1)"))# == True, "Simple"
    #print( checkio("{[(3+1)+2]+}"))# == True, "Different types"
    print( checkio("(3+{1-1)}"))# == False, ") is alone inside {}"
    print( checkio("[1+1]+(2*2)-{3/3}"))# == True, "Different operators"
    print( checkio("(({[(((1)-2)+3)-3]/3}-3)"))# == False, "One is redundant"
    print( checkio("2+3")) == True, "No brackets, no problem"
