def longest_palindromic(text):
    flag = False
    max_str = main_max = ''
    text3 = text[0:]
    for index, value in enumerate(text):
        # print(text[index:], end='=')
        # print(text[:-index])
        # print()
        text1 = text[:index+1]
        len_count1 = int(len(text1) / 2) if len(text1) % 2 == 0 else int(len(text1) / 2) + 1
        for i in range(len_count1):
            # print(text[i], text[len(text)-i-1], end='===\n')
            # if text1[i] == text1[len(text1)-i-1] == ' ':
            #     continue
            if (text1[i] != text1[len(text1)-i-1]) and flag == True:
                max_str = ''
                break
            if text1[i] == text1[len(text1)-i-1]:
                if (flag == False) and len(max_str) < len(text1[i:len(text1) - i]):
                    max_str = text1[i:len(text1)-i]
                flag = True
        if max_str != '' and len(main_max) < len(max_str):
            main_max = max_str
        # print(main_max)
        flag = False
        max_str = ''

    for index, value in enumerate(text):
        text2 = text[len(text) - index - 1:]
        len_count2 = int(len(text2) / 2) if len(text2) % 2 == 0 else int(len(text2) / 2) + 1
        for i in range(len_count2):
            # print(text[i], text[len(text)-i-1], end='===\n')
            # if text2[i] == text2[len(text2)-i-1] == ' ':
            #     continue
            if (text2[i] != text2[len(text2)-i-1]) and flag == True:
                max_str = ''
                break
            if text2[i] == text2[len(text2)-i-1]:
                if (flag == False) and len(max_str) < len(text2[i:len(text2)-i]):
                    max_str = text2[i:len(text2)-i]
                flag = True
        if max_str != '' and len(main_max) < len(max_str):
            main_max = max_str
        # print(main_max)
        flag = False
        max_str = ''



    return main_max

if __name__ == '__main__':
    print(longest_palindromic("artrartrt"))# == "rtrartr", "The Longest"
    print(longest_palindromic("abacada"))# == "aba", "The First"
    print(longest_palindromic("aaaa"))# == "aaaa", "The A"
    print(longest_palindromic("abc"))# == "a", "The A"
    print(longest_palindromic(" a b c "))# == "a", "The A"
    print(longest_palindromic("abacada"))# == "aba", "The A"
    print(longest_palindromic(" a b c"))# == "aba", "The A"
