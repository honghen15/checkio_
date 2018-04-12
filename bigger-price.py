import operator

def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    dict_name_price = {}
    list_right_answer = []
    count = 0
    for n in data:
        dict_name_price[n['name']]= n['price']
    #print(dict_name_price)
    # your code here
    sorted_data = sorted( dict_name_price.items(), key=operator.itemgetter(1), reverse=True )
    #print((sorted_data[0]))
    for tuple_data in sorted_data:
        if not(count==limit) :
            count+=1
        else:
            break
        list_right_answer.append( {'name':tuple_data[0], 'price':tuple_data[1]})

    #print(list_right_answer)
    # print(sorted_data)
    # for dict1 in data:
    #     pprint(dict1)
    return list_right_answer


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    pprint( bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) )
    #== [
    #     {"name": "wine", "price": 138},
    #     {"name": "bread", "price": 100}
    # ], "First"

    pprint( bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) )
    # == [{"name": "whiteboard", "price": 170}], "Second"
    #
    # print('Done! Looks like it is fine. Go and check it')
