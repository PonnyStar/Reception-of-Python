s = input('введите номер банковской карты (16 цифр): ')
number = ''.join(s.strip().split())
print(number[:4], '*'*4, '*'*4, number[-4:])
