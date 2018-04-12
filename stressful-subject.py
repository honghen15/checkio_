def is_stressful(subj):
    flag = True
    if (subj[-1]==subj[-2]==subj[-3]=='!'):
        return True
    subjj = ''
    for i in subj:
        if i.isalpha() is True:
            if i.islower():
                flag = False
            if len(subjj)==0 or i != subjj[-1]:
                subjj += i
    subjj = subjj.lower()
    print('==='+subjj)
    if ('help' in subjj)or( 'asap' in subjj)or( 'urgent'in subjj) or flag is True:
        return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(is_stressful("Hi"))# == False, "First"
    print(is_stressful("HI HOW ARE YOU"))# == False, "First"
    print(is_stressful("I neeed HELP"))# == True, "Second"
    print('Done! Go Check it!')
