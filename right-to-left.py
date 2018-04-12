def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """

    #correct_list = [ str_right.replace('right','left') for str_right in phrases if 'right' in str_right]
    correct_list = []
    #print( len(phrases))
    for str_right in phrases:
        #print(str_right)

        if 'right' in str_right:
            str_right = str_right.replace('right', 'left')
            correct_list.append(str_right)
        else:
            correct_list.append(str_right)
        #print('=================')
        #print(correct_list)


    #print(correct_list)
    str_sentence = ','.join( correct_list)
    return str_sentence

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( left_join(("left", "right", "left", "stop")))# == "left,left,left,stop", "All to left"
    print( left_join(("bright aright", "ok")))# == "bleft aleft,ok", "Bright Left"
    print( left_join(("brightness wright",)) )#== "bleftness wleft", "One phrase"
    print( left_join(("enough", "jokes")) )#== "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
