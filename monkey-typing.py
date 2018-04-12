def count_words(text, words):
    count = 0
    for i in words:
        if i in text.lower():
            count +=1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))# == 3, "Example"
    print( count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))# == 2, "BANANAS!"
    print( count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}))# == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
