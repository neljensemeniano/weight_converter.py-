def pounds_to_kilograms(weight):
    return weight * 0.453592

def kilograms_to_pounds(weight):
    return weight * 2.20462

print("1. Перевод фунтов в килограммы.")
print("2. Перевод килограммов в фунты.")
choice = int(input("Выберите режим (1 или 2): "))

if choice == 1:
    weight = float(input("Введите вес в фунтах: "))
    print(weight, "фунтов =", pounds_to_kilograms(weight), "килограмм.")
elif choice == 2:
    weight = float(input("Введите вес в килограммах: "))
    print(weight, "килограмм =", kilograms_to_pounds(weight), "фунтов.")
else:
    print("Ошибка ввода.")
