# Napisz prosty kalkulator BMI (Body Mass Index), który obliczy wskaźnik masy
# ciała na podstawie podanych przez użytkownika danych: masy ciała (w kilogramach) i wzrostu (w metrach).
#
# Zapytaj użytkownika o jego wagę (w kilogramach) i wzrost (w metrach).
# Oblicz BMI na podstawie wzoru: BMI = masa_ciała / (wzrost^2).
# Na podstawie uzyskanego BMI wyświetl komunikat informujący o stanie zdrowia użytkownika:
# BMI poniżej 18.5: "Niedowaga"
# BMI od 18.5 do 24.9: "Prawidłowa masa ciała"
# BMI od 25.0 do 29.9: "Nadwaga"
# BMI powyżej 30.0: "Otyłość"

def oblicz_BMI(weight, height):

    bmi = weight / (height ** 2)

    if weight > 40 and weight < 150:
        return bmi
    elif height > 1.4 and height < 2.1:
        return bmi
    else:
        return False

def kalkulator_BMI(bmi):


    if bmi:
        if bmi <= 18.5:
            return "Masz niedowagę"
        elif  bmi > 18.5 and bmi <= 25:
            return "Masz prawidłową masę ciała"
        elif bmi > 25 and bmi <= 30:
            return "Masz nadwagę"
        elif bmi > 30:
            return "Jesteś otyły"
    else:
        return "Złe dane"


while True:

    print("Witaj w kalkulatorze BMI. Wybierz co chcesz zrobić: ")
    print("1. Chcę obliczyć BMI")
    print("2. Chcę zakońćzyć program")


    try:
        wybor = int(input("Wpisz numer operacji:"))
        if wybor == 1:
            wejscie1 = float(input("Wprowadź swoją wagę: "))
            wejscie2 = float(input("Wprowadź swój wzrost: "))
            wejscie3 = oblicz_BMI(wejscie1, wejscie2)
            print(kalkulator_BMI(wejscie3))
        elif wybor == 2:
            print("Do zobaczenia!")
            break
        else:
            print("Nie ma takiej operacji. Wybierz numer 1 lub 2.")
    except ValueError:
        print("Nieprawidłowy numer operacji. Wybierz numer 1 lub 2")
