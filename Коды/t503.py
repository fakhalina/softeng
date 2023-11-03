from math import sqrt
def area(a, b, c):
    p = (a + b + c)/2
    s = sqrt(p * (p -a) * (p - b) * (p -c))
    return s
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
a1, a2 = max(one), min(one)
b1, b2 = max(two), min(two)
c1, c2 = max(three), min(three)

print('Площадь треугольника из макс элементов: ', area(a1, b1, c1))
print('Площадь треугольника из мин элементов: ', area(a2, b2, c2))

