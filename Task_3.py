# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)
x = int(input('Введите x (любое целое число, не равное 0): '))
y = int(input('Введите y (любое целое число, не равное 0): '))
if x > 0 and y > 0:
    print("Номер четверти плоскости: 1")
elif x < 0 and y > 0:
    print("Номер четверти плоскости: 2")
elif x < 0 and y < 0:
    print("Номер четверти плоскости: 3")
elif x > 0 and y < 0:
    print("Номер четверти плоскости: 4")
else:
    print("Ошибка ввода! Введите любое целое число, не равное 0!")


