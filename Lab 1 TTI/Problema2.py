def gaseste_maxim_aparitii(lista: list) -> tuple:
    res = max(set(lista), key=lista.count)
    count = 0
    for i in lista:
        if res == i:
            count += 1
    pereche = res, count
    return pereche
