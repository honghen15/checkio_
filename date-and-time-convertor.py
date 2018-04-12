import re

month_dic = { 1:'January', 2:'Febnuary', 3:'March', 4:'April', 5:'May', 6:'June',
              7:'July', 8:'August', 9:'September', 10:'October', 11:'November',
              12:'December'}
def date_time(time):
    #replace this for solution
    pattern = re.compile(r'(\d{2}).(\d{2}).(\d{4}) (\d{2}):(\d{2})')
    result = pattern.match(time)
    #print( '0:{%B}'.format('5', "month"))
    day = str(int(result.group(1)))
    month = month_dic[int(result.group(2))]
    year = str(int(result.group(3)))
    hour = str(int(result.group(4))) + (' hour' if ((int(result.group(4)))==1) else ' hours')

    minute = str(int(result.group(5))) + (' minute' if ((int(result.group(5))==1)) else ' minutes')
    str1 = '{0} {1} {2} year {3} {4}'.format(day, month, year, hour, minute)
    return str1
if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( date_time("01.01.2000 00:00"))# == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    print( date_time("09.05.1945 06:30"))# == "9 May 1945 year 6 hours 30 minutes", "Victory"
    print( date_time("20.11.1990 03:55"))# == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print( date_time("11.04.1812 01:01"))# == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
