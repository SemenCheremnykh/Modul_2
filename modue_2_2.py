namber_1=input('Введите первое число: ')
namber_2=input('Введите второе число: ')
namber_3=input('Введите третье число: ')
if namber_1==namber_2 and namber_1==namber_3 and namber_2==namber_3: #Проверяю условия равенства сразу трех чисел
    print('3')
elif namber_1!=namber_2 and namber_1!=namber_3 and namber_2!=namber_3: #Проверяю условия НЕравенства всех чисел
    print('0')
elif namber_1==namber_2 or namber_1==namber_3 or namber_2==namber_3: # Проверяю условия равенства хотябы двух чисел
    print ('2')