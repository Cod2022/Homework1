# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
for i in range(1):
    x1 = int(input("Введите X для точки A: "))
    y1 = int(input("Введите Y для точки A: "))
    x2 = int(input("Введите X для точки B: "))
    y2 = int(input("Введите Y для точки B: "))
num1 = (x2 - x1) ** 2
num2 = (y2 - y1) ** 2
sum = num1 + num2
result = sum ** 0.5
print(f"Расстояние между точками A и B = {round(result, 2)}")