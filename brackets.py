def checkio(expression):
    bracket_ = ''
    for i in expression:
        #print(i, bracket_)
        if (( i == '(' ) or (i == '[') or (i == '{') ):
            bracket_+=i
        elif ( i == ')' ):
            if len(bracket_) == 0:
                return False
            if bracket_[-1] == '(':
                bracket_ = bracket_[0:-1]
            else :
                return False
        elif i == ']':
            if len(bracket_) == 0:
                return False
            elif bracket_[-1] == '[':
                bracket_ = bracket_[0:-1]
            else :
                return False
        elif i == '}':
            if len(bracket_) == 0:
                return False
            if bracket_[-1] == '{':
                bracket_ = bracket_[0:-1]
            else :
                return False
    if bracket_ == '':
        return True
    #print(bracket['()'])


    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print( checkio("((5+3)*2+1)"))# == True, "Simple"
    # print( checkio("{[(3+1)+2]+}"))# == True, "Different types"
    # print( checkio("(3+{1-1)}"))# == False, ") is alone inside {}"
    # print( checkio("[1+1]+(2*2)-{3/3}"))# == True, "Different operators"
    # print( checkio("(({[(((1)-2)+3)-3]/3}-3)"))# == False, "One is redundant"
    # print( checkio("2+3")) #== True, "No brackets, no problem"
    # print( checkio("{[(3+1)+2]+}"))# == True, "No brackets, no problem"
    print( checkio("(((1+(1+1))))]"))# == True, "No brackets, no problem"
