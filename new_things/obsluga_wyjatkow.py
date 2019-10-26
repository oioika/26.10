zmienna_1 = input("Podaj liczbę: ")
zmienna_2 = input("Podaj liczbę: ")

try:
    a = int(zmienna_1)
    b = int(zmienna_2)
    # zmienna_integer = int(zmienna)
    # print(f"To jest liczba: {zmienna_integer}.")
    print(f"Suma liczb to: {a + b}.") #co tu jest źle?
except Exception:
    print("Nie byłem w stanie zrzutowac na inta")


print("Koniec")
