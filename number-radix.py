def checkio(str_number, radix):
    dict_base = { '0':0, '1':1,'2':2,'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
                  'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17,
                  'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25,
                  'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33,
                  'Y':34, 'Z':35}
    num = 0
    if(str_number.isdigit()):
        if(int(str_number) == 0):
            return 0
    for n in range(len(str_number)):
        if ( dict_base[str_number[len(str_number)-n-1]] >= radix ):
            return -1
        num+= dict_base[str_number[len(str_number)-n-1]]*(radix**n)
    return num

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print( checkio("AF", 16) )#== 175, "Hex"
    print( checkio("101", 2) )#== 5, "Bin"
    print( checkio("101", 5) )#== 26, "5 base"
    print( checkio("Z", 36) )#== 35, "Z base"
    print( checkio("AB", 10) )#== -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
