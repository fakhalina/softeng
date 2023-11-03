list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
def pravilo(a):
    a.sort()
    list = []
    number = a[0]
    str1 = ""
    for item in a:
        if number == item:
            number = item
            str1 += str(item)
            list.append(str1)
        else:
            number = item
            str1 = ""
            str1 += str(item)
            list.append(str1)
    for item in list:
        if len(item) == 1:
            list.remove(item)
            list.insert(0, int(item))
    print(list)
pravilo(list_1)
pravilo(list_2)
pravilo(list_3)