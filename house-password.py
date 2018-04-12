import re

def checkio(data):
    #pattern = re.findall(r"([a-zA-Z0-9]+){10}", data)
    #replace this for solution
    match1 = False
    match2 = False
    match3 = False
    for i in range(len(data)):
        if data[i].islower():
            match1 = True
        if data[i].isupper():
            match2 = True
        if data[i].isnumeric():
            match3 = True
    if match1 and match2 and match3 and len(data)>=10:
        return True
    #print(pattern)
    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( checkio('A1213pokl'))# == False, "1st example"
    print( checkio('bAse730onE'))# == True, "2nd example"
    print( checkio('asasasasasasasaas'))# == False, "3rd example"
    print( checkio('QWERTYqwerty'))# == False, "4th example"
    print( checkio('123456123456'))# == False, "5th example"
    print( checkio('QwErTy911poqqqq'))# == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
