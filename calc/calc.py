While True:
    print(1.'+')
    print(2.'-')
    print(3.'*')
    print(4.'/')
    print(5.'**')
    print(6.'%')
    print(7.'//')
    print(0.'Выход')
    choice == '0':

        print('Пока!')
        break

    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print('Нет такого пункта.')
        continue

    a = float(input('Первое число: '))
    b = float(input('Второе число: '))

    if choice in ['4', '6', '7'] and b == 0:
        print('Ошибка. На ноль делить нельзя.')
        continue
    if choice == '1': res = a + b
    elif choice == '2': res = a - b
    elif choice == '2': res = a * b
    elif choice == '2': res = a / b
    elif choice == '2': res = a ** b
    elif choice == '2': res = a % b
    elif choice == '2': res = a // b

    print('результат:', res)

    if res > 100:
        print('Высокое значение.)
