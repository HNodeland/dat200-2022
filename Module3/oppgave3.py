#Likesidet trekant
#del sidene inn i 3 like store deler
#lag en ny likesidet trekant med det midterste linjestykket som utgangspunkt.
    #denne trekanten har sider som er 1/3 fra parent-trekanten
    #peker vekk fra parent-trekanten
#slett det midterste linjestykket som ble brukt som utgangspunkt i forrige steg

from turtle import *
speed(0)


def snowFlake(length, degree):
    if degree == 0:
        forward(length)
        return
    length /= 3.0
    snowFlake(length, degree-1)
    left(60)
    snowFlake(length, degree-1)
    right(120)
    snowFlake(length, degree-1)
    left(60)
    snowFlake(length, degree-1)

for i in range(3):

    snowFlake(100, 2)
    right(120)


done()