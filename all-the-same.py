from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    same = None
    for i in elements:
        #print(i)
        if same == None:
            same = i
        elif not same == i :
            return False
    return True
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    print( all_the_same([1, 1, 1]))# == True
    print( all_the_same([1, 2, 1]))# == False
    print( all_the_same(['a', 'a', 'a']))# == True
    print( all_the_same([]))# == True
    print( all_the_same([1]))# == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
