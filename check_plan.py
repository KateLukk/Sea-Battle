print('Для начала игры расставьте корабли')
print('1 - занятая кораблем клетка, 0 - пустая')

pole = []
tekush_stroka = 0
k = True
kolvo_kletok = 0
korabli = {1: 0, 2: 0, 3: 0, 4: 0}

for i in range(10):
    pole.append([int(j) for j in input().split()])
for i in range(10):
    for j in range(10):
        if pole[i][j] == 1:
            kolvo_kletok += 1
        if pole[i][j] != 1 and pole[i][j] != 0:
            k = False
            print('Перечитайте инструкцию выше')

if kolvo_kletok != 20 and k:
    if kolvo_kletok > 20:
        print("Кораблями занято слишком много клеток")
    else:
        print("Кораблями занято слишком мaло клеток")

elif kolvo_kletok == 20 and k:
    for i in range(10):
        for j in range(10):
            if k:
                if pole[i][j] == 1:
                    tekush_stroka += 1

                if (pole[i][j] == 0 or j == 9) and tekush_stroka != 0:

                    if tekush_stroka > 4:
                        k = False
                        print("Корабль не может занимать больше 4 клеток")

                    elif tekush_stroka > 1:
                        korabli[tekush_stroka] += 1
                        t = tekush_stroka
                        tekush_stroka = 0

                        if i != 0 and i != 9:
                            c1 = pole[i - 1][j - t:j + 1].count(1)
                            c2 = pole[i + 1][j - t:j + 1].count(1)
                            if c1 != 0 or c2 != 0:
                                k = False
                                print('Корабли расставлены невeрно')

                        elif i == 0:
                            t = tekush_stroka
                            c2 = pole[i + 1][j - t:j + 1].count(1)
                            if c2 != 0:
                                k = False
                                print('Корабли расставлены невeрно')
                        elif i == 9:
                            t = tekush_stroka
                            c2 = pole[i - 1][j - t:j + 1].count(1)
                            if c2 != 0:
                                k = False
                                print('Корабли расставлены невeрно')

                    elif tekush_stroka == 1:
                        if i != 0 and i != 9:
                            if j != 9:
                                if pole[i - 1][j - 1] == pole[i + 1][j - 1] == 0:
                                    korabli[tekush_stroka] += 1
                            if j == 9:
                                if pole[i - 1][j] == pole[i + 1][j] == 0:
                                    korabli[tekush_stroka] += 1
                        elif i == 0:
                            if j != 9:
                                if pole[i + 1][j - 1] == 0:
                                    korabli[tekush_stroka] += 1
                            if j == 9:
                                if pole[i + 1][j] == 0:
                                    korabli[tekush_stroka] += 1
                        elif i == 9:
                            if j != 9:
                                if pole[i - 1][j - 1] == 0:
                                    korabli[tekush_stroka] += 1
                            if j == 9:
                                if pole[i - 1][j] == 0:
                                    korabli[tekush_stroka] += 1
                    tekush_stroka = 0

            else:
                break
    tekush_stroka = 0

    for j in range(10):
        for i in range(10):
            if k:
                if 0 < i < 9:
                    if pole[i][j] == 1 and (pole[i + 1][j] == 1 or pole[i - 1][j] == 1):
                        tekush_stroka += 1
                elif i == 0:
                    if pole[i][j] == 1 and pole[i + 1][j] == 1:
                        tekush_stroka += 1
                elif i == 9:
                    if pole[i][j] == 1 and pole[i - 1][j] == 1:
                        tekush_stroka += 1
                if (pole[i][j] == 0 or i == 9) and tekush_stroka != 0:
                    if tekush_stroka > 4:
                        k = False
                        print("Корабль не может занимать больше 4 клеток")
                    elif tekush_stroka > 1:
                        korabli[tekush_stroka] += 1
                        tekush_stroka = 0



    if k and korabli[1] == 4 and korabli[2] == 3 and korabli[3] == 2 and korabli[4] == 1:
        print('Корабли расставлены верно!!! УРА!')
    else:
        if k:
            print('Корабли расставлены невeрно')
