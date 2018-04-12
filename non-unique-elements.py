#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    list1 = []
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  
    data.count(data[0])
    print( data.count(data[0]))
    for i in data :
        if data.count(i)>1:
            list1.append(i)
    #replace this for solution

    return list1

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( list(checkio([1, 2, 3, 1, 3])))# == [1, 3, 1, 3], "1st example"
    print( list(checkio([1, 2, 3, 4, 5])))# == [], "2nd example"
    print( list(checkio([5, 5, 5, 5, 5])))# == [5, 5, 5, 5, 5], "3rd example"
    print( list(checkio([10, 9, 10, 10, 9, 8])))# == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")#