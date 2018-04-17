import re
import numpy as np
def checkio(data):
    tuple1 = re.findall(r'((\d+),(\d+))', data)
    y1 = int(tuple1[0][2])-int(tuple1[1][2])
    x1 = int(tuple1[0][1])-int(tuple1[1][1])
    y2 = int(tuple1[1][2])-int(tuple1[2][2])
    x2 = int(tuple1[1][1]) - int(tuple1[2][1])
    ans1 = y1*(int(tuple1[0][2])+int(tuple1[1][2]))/2+x1*(int(tuple1[0][1])+int(tuple1[1][1]))/2
    ans2 = y2*(int(tuple1[1][2])+int(tuple1[2][2]))/2+x2*(int(tuple1[1][1])+int(tuple1[2][1]))/2
    list = [y1,x1], [y2,x2]
    list_ans = [ans1, ans2]
    a = np.array(list)
    b = np.array(list_ans)
    x = np.linalg.solve(a, b)
    # print(int(tuple1[1][2]) - int(tuple1[0][2]))
    # print(tuple1[1][2]) - int(tuple1[0][2]))
    #replace this for solution
    distance = (x[1]-int(tuple1[0][1]))**2+(x[0]-int(tuple1[0][2]))**2
    distance = round(distance**0.5, 2)
    distance = round(distance, 2) if distance > int(distance) else int(distance)
    if x[0] == int(x[0]):
        aa = int(x[0])
    else:
        aa = round(x[0],2)
    if x[1] == int(x[1]):
        bb = int(x[1])
    else:
        bb = round(x[1],2)
    return '(x-{0})^2+(y-{1})^2={2}^2'.format(bb, aa, distance)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("(2,2),(6,2),(2,6)"))# == "(x-4)^2+(y-4)^2=2.83^2"
    print(checkio("(3,7),(6,9),(9,7)"))# == "(x-6)^2+(y-5.75)^2=3.25^2"
    print(checkio("(7,7),(4,3),(1,8)"))# == "(x-6)^2+(y-5.75)^2=3.25^2"
