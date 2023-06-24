# zadanie 1.1

hello = "Hello"
student = "Ola"

print("{} {}".format(hello, student))



# zadanie 1.2

print('Wpisz swoje imie')

imie = input()

print(type(imie))
print("Hello"+' '+imie)



# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci).__str__()

print("Liczba studentow wynosi: " + liczba_studentow)



# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in studenci:
    
    print("hello "+i)



# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba**potega

print("Wynik wynosi: "+str(wynik))



# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))



# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: "+ str(studenci))



# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda name: name.split(" ")[-1].lower())

print(studenci)



# zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_studentow = 0

for student in studenci:
    
    if student.split()[1][0] == "N":
        
        liczba_studentow += 1

print("Liczba studentów na N wynosi: ", liczba_studentow)




# zadanie 1.10

def czy_istnieje_funkcja_liniowa(wykres):

    wspolrzedne_x = [punkt[0] for punkt in wykres]
    wspolrzedne_y = [punkt[1] for punkt in wykres]

    if len(set(wspolrzedne_x)) == 1:

        return True

    liczba_punktow = len(wykres)

    suma_x = sum(wspolrzedne_x)
    suma_y = sum(wspolrzedne_y)

    suma_xy = sum(wspolrzedne_x[i] * wspolrzedne_y[i] for i in range(liczba_punktow))
    suma_x2 = sum(wspolrzedne_x[i] ** 2 for i in range(liczba_punktow))

    a = (liczba_punktow * suma_xy - suma_x * suma_y) / (liczba_punktow * suma_x2 - suma_x ** 2)
    b = (suma_y - a * suma_x) / liczba_punktow

    for i in range(liczba_punktow):

        if wspolrzedne_y[i] == a * wspolrzedne_x[i] + b:

            return True

    return False


wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

wykres_1_funkcja_liniowa = czy_istnieje_funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = czy_istnieje_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_istnieje_funkcja_liniowa(wykres_3)



if wykres_1_funkcja_liniowa:
    
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")

else:
    
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")


if wykres_2_funkcja_liniowa:
    
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")

else:
    
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")


if wykres_3_funkcja_liniowa:
    
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")

else:
    
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")