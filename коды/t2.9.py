#Найти площадь и полупериметр треугольника, ввести значения сторон через консоль
a, b, c = int(input('a=')), int(input('b=')), int(input('c='))
p = (a + b +c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print('p=', p)
print('s=', s)
