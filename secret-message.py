def find_message(text):
    """Find a secret message"""
    secretStr = ''
    for i in range(len(text)):
        if text[i].isupper():
            #print(text[i])
            secretStr+= text[i]
    #print(secretStr)
    return secretStr

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( find_message("How are you? Eh, ok. Low or Lower? Ohhh."))# == "HELLO", "hello"
    print( find_message("hello world!") )#== "", "Nothing"
    print( find_message("HELLO WORLD!!!") )#== "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
