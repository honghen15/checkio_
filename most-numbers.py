import operator
def checkio(*args):
    try:
        if not args == '':
            max_value = max(args)
            min_value = min(args)
        #print(max_value, min_value)
        #print( '===', end='')
        #print(round(max_value-min_value, 3))
        return max_value-min_value
    except ValueError:
        return int(0)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        #return correct - precision < checked < correct + precision

        return round(checked, int(significant_digits)) if not checked=='' else ''

    print( almost_equal(checkio(1, 2, 3), 2, 3))#, "3-1=2"
    print( almost_equal(checkio(5, -5), 10, 3))#, "5-(-5)=10"
    print( almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3))#, "10.2-(-2.2)=12.4"
    print( almost_equal(checkio(), 0, 3))#, "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
