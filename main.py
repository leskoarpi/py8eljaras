'''
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
'''
def nagyobb(szam1,szam2):
    if int(szam1) != int(szam2) and int(szam1)>int(szam2):
        print(szam1)
    elif szam1 < szam2:
        print(szam2)
    else:
        print('egyenlo')

nagyobb(9,8)