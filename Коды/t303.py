one = int(input('Введите значение пременной: '))
if one<0 or one>10:
    print("Число вне диапозона")
elif one>=0 and one<4:
    print('Число находится в диапозоне от 0 до 3 вкл.')
elif one>3 and one<6:
    print('Число в диапозоне от 3 до 6')
elif one > 6 and one <= 10:
    print('Число от 6 до 10 вкл')
