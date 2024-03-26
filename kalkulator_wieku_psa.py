# Zadanie: Kalkulator wieku psa
# Napisz prosty program, który obliczy wiek psa w psich latach na podstawie jego wieku w ludzkich latach. Zwykle mówi się, że pierwsze dwa lata życia psa odpowiadają około 10,5 ludzkiego roku, a każdy kolejny rok psa odpowiada około 4 ludzkich latom.
#
# Wskazówki:
# Poproś użytkownika o podanie wieku swojego psa w ludzkich latach.
# Użyj podanych proporcji, aby obliczyć wiek psa w psich latach.
# Wydrukuj wynik.

import math as math

def wiek_psa(wiek):
    wiek_psa = 16 * math.log(wiek) + 31
    return wiek_psa

wejscie = int(input("Podaj wiek swojego psa w latach ludzkich: "))
wiek = wiek_psa(wejscie)

print("Wiek twojego psich latach:", round(wiek, 0))

