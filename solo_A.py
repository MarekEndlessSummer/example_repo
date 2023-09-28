import math

# Definicja funkcji

def objetosc_i_pole_szescianu(a):
    objetosc = a ** 3
    pole_powierzchni = 6 * (a ** 2)
    return objetosc, pole_powierzchni

def objetosc_kuli(r):
    objetosc = (4/3) * math.pi * (r ** 3)
    return objetosc

# Testy

def test_funkcji_szescianu():
    assert objetosc_i_pole_szescianu(3) == (27, 54)
    assert objetosc_i_pole_szescianu(4) == (64, 96)


def test_funkcji_kuli():
    assert math.isclose(objetosc_kuli(3), 113.097, rel_tol=1e-3)
    assert math.isclose(objetosc_kuli(4), 268.083, rel_tol=1e-3)


# Uruchomienie testów

if __name__ == "__main__":
    test_funkcji_szescianu()
    test_funkcji_kuli()
    print("Wszystkie testy przeszły pomyślnie.")
