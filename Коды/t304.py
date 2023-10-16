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
