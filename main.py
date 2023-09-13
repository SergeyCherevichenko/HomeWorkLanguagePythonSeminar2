
def task10():

    # На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
    # монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
    # количество монет, которые нужно перевернуть.

    n = int(input("Введите количество монеток: "))
    print("Если монетка лежит вверхом (решкой) то введите цифру 1, а если наоборот низом (гербом) то введите цифру 0")
    sum0 = 0
    sum1 = 0
    for i in range(n):
        number = int(input("Введите 1 или 0: "))
        if number == 0:
            sum0 += 1
        else:
            sum1 += 1
    if sum0 > sum1:
        print(f"Минимально необходимо перевернуть {sum1} монеток")
    else:
        print(f"Минимально необходимо перевернуть {sum0} монеток")

def task12():

    #        Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
    # натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
    # произведение P. Помогите Кате отгадать задуманные Петей числа.

    print("Петя загадал два натуральных числа (от 1 до 1000 включительно)!")
    print("Катя должна отгадать эти числа!")
    print("Петя дает подсказки: ")
    sum = int(input("Введите сумму этих чисел: "))
    mult = int(input("Введите произведение этих чисел: "))
    print(f"x + y = {sum}")
    print(f"x * y = {mult}")

    print("Катя отвечает: ")
    ex = False
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (x + y == sum and x * y == mult):
                print(x, y)
                ex = True
    if not ex : print("Не правильный ввод данных!")

def task14():

    # Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.

    n = int(input("Введите ваше целое число: "))
    i = 1
    while i < n:
        print(i, end=" ")
        i = i * 2


task = int(input("Введите номер задачи 10, 12 или 14: "))
if task == 10:
    task10()
elif task == 12:
    task12()
elif task == 14:
    task14()
else:
    print("Задачи с таким номером не существует!")


