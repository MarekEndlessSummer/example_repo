class Samochod:
    def __init__(self, marka, model, rocznik, kolor, predkosc_max, aktualna_predkosc=0):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.kolor = kolor
        self.predkosc_max = predkosc_max
        self.aktualna_predkosc = aktualna_predkosc

    def __str__(self):
        return f"Samochód: {self.marka} {self.model}, Rocznik: {self.rocznik}, Kolor: {self.kolor}, Prędkość maksymalna: {self.predkosc_max} km/h, Aktualna prędkość: {self.aktualna_predkosc} km/h"

    def przyspiesz(self, ile_km_h):
        if self.aktualna_predkosc + ile_km_h <= self.predkosc_max:
            self.aktualna_predkosc += ile_km_h
        else:
            self.aktualna_predkosc = self.predkosc_max

    def zwolnij(self, ile_km_h):
        if self.aktualna_predkosc - ile_km_h >= 0:
            self.aktualna_predkosc -= ile_km_h
        else:
            self.aktualna_predkosc = 0

# Przykład użycia klasy Samochod
moj_samochod = Samochod("Toyota", "Corolla", 2022, "srebrny", 180)
print(moj_samochod)

moj_samochod.przyspiesz(40)
print(f"Aktualna prędkość po przyspieszeniu: {moj_samochod.aktualna_predkosc} km/h")

moj_samochod.zwolnij(20)
print(f"Aktualna prędkość po zwolnieni: {moj_samochod.aktualna_predkosc} km/h")