# trojkat
import math
Bok_a = 10
Bok_b = 20
Bok_c = 15
Wysokosc_h = 12

obwod_trojkat = Bok_a + Bok_b + Bok_c
pole_trojkat = int((Wysokosc_h * Bok_a) / 2)

print("Obwod trojkata wynosi " + str(obwod_trojkat) + ",  pole wynosi " + str(pole_trojkat) + ".")

obwod_prostokat = 2*Bok_a+2*Bok_b
pole_prostokat = Bok_a * Bok_b
print("Obwod prostokąta wynosi " + str(obwod_prostokat) + ", zas pole wynosi " + str(pole_prostokat) + ".")

Promien_r = 10;

obwod_kolo = 2*math.pi*Promien_r
pole_kolo = math.pi*Promien_r**2
print("Obwod koła wynosi " + str(obwod_kolo) + ", zas pole wynisi " + str(pole_kolo) + ".")

obwod_romb = 2*Bok_a+2*Bok_b
pole_romb = Bok_a*Wysokosc_h
print("Obwod romb wynosi " + str(obwod_romb) + ", zas pole wynisi " + str(pole_romb) + ".")