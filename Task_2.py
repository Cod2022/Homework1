# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
for i in range(1):
    x = int(input("Введите X: "))
    y = int(input("Введите Y: "))
    z = int(input("Введите Z: "))
a = not x is not y is not z
b = a
if b != False:
    print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно")
else:
    print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно")
