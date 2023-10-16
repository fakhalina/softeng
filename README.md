# Тема 3. Операторы, условия, циклы.
Отчет по Теме #3 выполнила:
- Фаухиева Алина Ильдаровна
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + | 
| Задание 8 | + | 
| Задание 9 | + | 
| Задание 10 | + | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте две переменные, значение которых будете вводить через консоль. Также составьте условие, в котором созданные ранее переменные будут сравниваться, если условие выполняется, то выведете в консоль «Выполняется», если нет, то «Не выполняется».

### Результат.
![Меню](pic/lt301.png)

## Лабораторная работа №2
### Напишите программу, которая будет определять значения переменной меньше 0, больше 0 и меньше 10 или больше 10. Это нужно реализовать при помощи одной переменной, значение которой будет вводится через консоль, а также при помощи конструкций if, elif, else.

### Результат.
![Меню](pic/lt302.png)

## Лабораторная работа №3
### Напишите программу, в которой будет проверяться есть ли переменная в указанном массиве используя логический оператор in. Самостоятельно посмотрите, как работает программа со значениями которых нет в массиве numbers.

### Результат.
![Меню](pic/lt303.png)

## Лабораторная работа №4
### Напишите программу, которая будет определять находится ли переменная в указанном массиве и если да, то проверьте четная она или нет. Самостоятельно протестируйте данную программу с разными значениями переменной value.

### Результат.
![Меню](pic/lt304.png)

## Лабораторная работа №5
### Напишите программу, в которой циклом for значения переменной i будут меняться от 0 до 10 и посмотрите, как разные виды сравнений и операций работают в цикле.

### Результат.
![Меню](pic/lt305.png)

## Лабораторная работа №6
### Напишите программу, в которой при помощи цикла for определяется есть ли переменная value в строке string и посмотрите, как работает оператор else для циклов. Самостоятельно посмотрите, что выведет программа, если значение переменной value оказалось в строке string

### Результат.
![Меню](pic/lt306.png)

## Лабораторная работа №7
### Напишите программу, в которой вы наглядно посмотрите, как работает цикл for проходя в обратном порядке, то есть, к примеру не от 0 до 10, а от 10 до 0. В уже готовой программе показано вычитание из 100, а вам во время реализации программы будет необходимо придумать свой вариант применения обратного цикла

### Результат.
![Меню](pic/lt307.png)

## Лабораторная работа №8
### Напишите программу используя цикл while, внутри которого есть какие-либо проверки, но быть осторожным, поскольку циклы while при неправильно написанных условиях могут становится бесконечными

### Результат.
![Меню](pic/lt308.png)

## Лабораторная работа №9
### Напишите программу с использованием вложенных циклов и одной проверкой внутри них. Самое главное, не забудьте, что нельзя использовать одинаковые имена итерируемых переменных, когда вы используете вложенные циклы

### Результат.
![Меню](pic/lt309.png)

## Лабораторная работа №10
### Напишите программу с использованием вложенных циклов и одной проверкой внутри них. Самое главное, не забудьте, что нельзя использовать одинаковые имена итерируемых переменных, когда вы используете вложенные циклы

### Результат.
![Меню](pic/lt310.png)

## Самостоятельная работа №1
### Напишите программу, которая преобразует 1 в 31. Для выполнения поставленной задачи необходимо обязательно и только один раз использовать: • Цикл for • *= 5 • += 1 Никаких других действий или циклов использовать нельзя
```python
one = 1
for i in range(2):
    one *=5
    one +=1
print(one)
```
### Результат.
![Меню](pic/t301.png)

## Вывод

## Самостоятельная работа №2
### Напишите программу, которая фразу «Hello World» выводит в обратном порядке, и каждая буква находится в одной строке консоли.
```python
str = 'Hello World'
for let in reversed(str):
    print(let)
```
### Результат.
![Меню](pic/t302.png)

## Вывод

## Самостоятельная работа №3
### Напишите программу, на вход которой поступает значение из консоли, оно должно быть числовым и в диапазоне от 0 до 10 включительно (это необходимо учесть в программе). Если вводимое число не подходит по требованиям, то необходимо вывести оповещение об этом в консоль и остановить программу. Код должен вычислять в каком диапазоне находится полученное число. 
```python
one = int(input('Введите значение пременной: '))
if one<0 or one>10:
    print("Число вне диапозона")
elif one>=0 and one<4:
    print('Число находится в диапозоне от 0 до 3 вкл.')
elif one>3 and one<6:
    print('Число в диапозоне от 3 до 6')
elif one > 6 and one <= 10:
    print('Число от 6 до 10 вкл')
```
### Результат.
![Меню](pic/t303.png)

## Вывод

## Самостоятельная работа №4
### Манипулирование строками. Напишите программу на Python, которая принимает предложение (на английском) в качестве входных данных от пользователя. Выполните следующие операции и отобразите результаты: • Выведите длину предложения.• Переведите предложение в нижний регистр. Подсчитайте количество гласных (a, e, i, o, u) в предложении. • Замените все слова "ugly" на "beauty". • Проверьте, начинается ли предложение с "The" и заканчивается ли на "end".
```python
str = input('Введите предложение на англ: ').lower()
a = 0
for let in str:
    if let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u':
        a += 1
rep_str = str.replace('ugly', 'beauty')
print(f'Длина предложения равна {len(str)}.\n'
      f'Количество гласных букв в предложении равно {a}.\n'
      f'Новое предложение:{rep_str}.\n'
      f'Предложение начинается с "The"?  {str.startswith("the")}.\n'
      f'Предложение заканчивается на "end"? {str.endswith("end")}')
```
### Результат.
![Меню](pic/t304.png)

## Вывод

## Самостоятельная работа №5
### Составьте программу, результатом которой будет данный вывод в консоль:
```python
values = [0, 2, 4, 6, 8, 10]
counter = 0
string = 'hello'
while counter !=10:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    string = memory
    counter += 1
memory = ' world'
print(string + memory)
```
### Результат.
![Меню](pic/t305.png)

## Вывод
