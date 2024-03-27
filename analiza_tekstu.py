# Napisz program, który analizuje tekst wprowadzony przez użytkownika i wykonuje następujące czynności:
#
# Oblicza liczbę słów w tekście.
# Oblicza liczbę zdań w tekście.
# Oblicza średnią długość słowa w tekście (w znakach).
# Wypisuje najczęściej występujące słowo w tekście.
# Wypisuje najczęściej występujący znak interpunkcyjny (., !, ?) oraz jego liczbę wystąpień.
# Wskazówki:
# Możesz użyć funkcji split() do podzielenia tekstu na słowa i funkcji len() do obliczenia liczby elementów w liście słów.
# Zdania często kończą się znakami interpunkcyjnymi, takimi jak ".", "!" lub "?".
# Aby obliczyć średnią długość słowa, możesz zsumować długość wszystkich słów i podzielić przez liczbę słów.
# Możesz użyć słownika do zliczenia wystąpień poszczególnych słów i znaków interpunkcyjnych.
# Po zliczeniu wszystkich słów i znaków interpunkcyjnych, możesz wybrać te, które występują najczęściej.


def analiza_tekstu(wejscie):

    liczba_slow = len(wejscie.split())

    liczba_zdań = 0
    znaki_interpunkcyjne = set(".!?")
    for znak in wejscie:
        if znak in znaki_interpunkcyjne:
            liczba_zdań = liczba_zdań + 1

    liczba_liter = 0
    for slowo in wejscie.split():
        liczba_liter += len(slowo)

    srednia_liczba = liczba_liter / len(wejscie.split())
    return liczba_slow, liczba_zdań, srednia_liczba


wejscie = input("Wpisz tekst: ")
wynik = analiza_tekstu(wejscie)

print("Liczba słów w twoim tekście wynosi:", wynik[0])
print("Liczba zdań w twoim tekście wynosi:", wynik[1])
print("Średnia liczba liter w słowie w twoim tekście wynosi:", wynik[2])
