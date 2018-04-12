def checkio(text):
    text = text.lower()
    dict1 = {}
    for i in text:
        if i.islower() and i in dict1.keys():
            dict1[i] +=1
        elif not i in dict1.keys() and i.islower():
            dict1[i] = 1
    #list1 = list(dict1.keys())
    #list2 = list(dict1.values())
    list3 = list(dict1.items())

    #print(list1)
    #print(list2)
    #print(list3)
    list1 = []
    for li1 in list3:
        if list1 ==[] or list1[0][1] == li1[1]:
            if list1 ==[] or list1[0][0] <= li1[0]:
                list1.append(li1)
            elif list1[0][0] > li1[0]:
                list1.insert(0,li1)
        elif list1[0][1] < li1[1]:
            list1 = [li1]

    #print(list1)
    #replace this for solution
    return list1[0][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( checkio("Hello World!"))# == "l", "Hello test"
    print( checkio("How do you do?"))# == "o", "O is most wanted"
    print( checkio("One"))# == "e", "All letter only once."
    print( checkio("Oops!"))# == "o", "Don't forget about lower case."
    print( checkio("AAaooo!!!!"))# == "a", "Only letters."
    print( checkio("abe"))# == "a", "The First."
    print("Start the long test")
    print( checkio("a" * 9000 + "b" * 1000))# == "a", "Long."
    print("The local tests are done.")
