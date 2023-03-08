import math
import random


def prog1():
    slova=[]
    while (n_slovo:=str(input())) != "stop":
        slova.append(n_slovo)
    print(" ".join(slova))
def prog2():
    a=[]
    while (stroka:=str(input())) !="stop":
        if "Ф" in stroka or "ф" in stroka:
            print("Ого!",stroka,"- редкое слово")
        else:
            print("Ох...", stroka, "-это обычное слово")
from random import randint
def prog3():
    try:
        res = 0
        popitky = 3
        vern_ot = 0
        while popitky != 0:
            c1 = randint(1, 12)
            c2 = randint(1, 12)
            znak_list = ['+', '-', '*', '/']
            znak = random.choice(znak_list)
            if znak == '+':
                res = c1 + c2
            if znak == '-':
                res = c1 - c2
            if znak == '*':
                res = c1 * c2
            if znak == '/':
                res = c1 // c2
                res=math.floor(res)
            if znak=='/':
                print("округлите до целого")
                print(c1, znak, c2, "= ", end="")
                a = int(input())
                print(res)
            else:
                print(c1, znak, c2, "= ", end="")
                a = int(input())
            if res== a:
                print("верно!")
                vern_ot +=1
            else:
                print("неверно.")
                popitky -= 1
        print("Увы,вы проиграли. Верных ответов: ",vern_ot)
    except Exception:
        print("ошибка")
prog1()
prog2()
prog3()