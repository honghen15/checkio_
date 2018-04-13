def checkio(n, m):


    str1 = bin(n)[2:] if (len(bin(n))> len(bin(m))) else  bin(m)[2:]
    str2 = bin(n)[2:] if (len(bin(n))<= len(bin(m))) else  bin(m)[2:]

    if len(str1)>len(str2):
        str2 = '0'*(len(str1)-len(str2)) + str2
    else :
        str1 = '0'*(len(str2)-len(str1)) + str1
    count = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count+=1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( checkio(117, 17))# == 3, "First example"
    print( checkio(1, 2))# == 2, "Second example"
    print( checkio(16, 15))# == 5, "Third example"
