import random

def main():
    value = random.randint(1, 6)
    print('На кубике выпало число: ', value)

    if (value == 5 or 6):
        print('Вы выиграли')
    elif value == 1 or 2:
        print('Вы проиграли')
    else:
        main()

if __name__ == '__main__':
    main()
