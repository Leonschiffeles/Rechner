import math


def circle_area():
    rad = float(input("Укажите радиус ==>"))
    s_circle = 3.14 * rad ** 2
    print(f"Площадь круга с радиусом >{rad}< составляет >{s_circle}<")


def tri_area():
    side = float(input("Значение cтороны   ==>"))
    base = float(input("Значение оснований ==>"))
    hieght = float(input("Введите высоту ==>"))
    heig = math.sqrt(side ** 2 - (base / 2) ** 2)
    if hieght == 0:
        hieght = heig
    r_area = 0.5 * base * hieght
    print(f"Площадь треугольник со сторонами :>{side}< \n"
          f"основанием:>{base}< высотой:>{hieght}<\n"
          f" составляет: >{r_area}<")


def squ_area():
    side = float(input("Введите сторону квадрата"))
    s_squer = side ** 2
    print(f"Площадь квадрата со сторонами >{side}< составляет >{s_squer}<")


while True:
    ptn = input("...Для расчёта площади \n"
                "круга введите    ==> C \n"
                "рвб-треугольника ==> T \n"
                "квадрата введите ==> S \n"
                "Bаш выбор=.......==>")

    if ptn == "C":
        circle_area()
    elif ptn == "T":
        tri_area()
    elif ptn == "S":
        squ_area()
    else:
        print("Hекорректное значение ввода\n"
              "Используйте только значение\n"
              ">>> C <<>>> T <<<>>> S <<<")
