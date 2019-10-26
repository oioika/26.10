def pobierz_liczbę():
    return int(input("Podaj liczbę"))

def wsadz_do_listy(element, lista):
    if element  < 10:
        lista.append(element)
    else:
        raise Exception(f"Element {element} jest większy niż 10")

nasza_lista = []
print(nasza_lista)
try:
    wsadz_do_listy(0, nasza_lista)
    print(nasza_lista)
    wsadz_do_listy(1, nasza_lista)
    print(nasza_lista)
    wsadz_do_listy(2, nasza_lista)
    print(nasza_lista)
    wsadz_do_listy(4, nasza_lista)
    print(nasza_lista)
    wsadz_do_listy(112, nasza_lista)
    print(nasza_lista)
    wsadz_do_listy(9, nasza_lista)
    print(nasza_lista)
except Exception as error:
    print(error)
    print(nasza_lista)