import math

# Aktualizacja definicji funkcji

def objetosc_stozka(r, h):
    objetosc = (1/3) * math.pi * (r ** 2) * h
    return objetosc

def objetosc_ostroslupa(B, h):
    objetosc = (1/3) * B * h
    return objetosc

# Aktualizacja testów

def test_funkcji_stozka():
    assert math.isclose(objetosc_stozka(3, 4), 37.699, rel_tol=1e-3)
    assert math.isclose(objetosc_stozka(4, 5), 83.776, rel_tol=1e-3)


def test_funkcji_ostroslupa():
    assert math.isclose(objetosc_ostroslupa(9, 4), 12, rel_tol=1e-3)
    assert math.isclose(objetosc_ostroslupa(16, 5), 26.667, rel_tol=1e-3)


# Aktualizacja uruchomienia testów

if __name__ == "__main__":
    test_funkcji_stozka()
    test_funkcji_ostroslupa()
    print("Wszystkie testy przeszły pomyślnie.")
