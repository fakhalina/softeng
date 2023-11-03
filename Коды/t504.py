def good(mark):
    my_list = []
    for item in mark:
        if item != 2:
            if item == 3:
                item = 4
            my_list.append(item)
    print(my_list)
a = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
c= [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
good(a)
good(b)
good(c)
