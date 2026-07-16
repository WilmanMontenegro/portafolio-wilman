def saber_si_hay_duplicados(lista):
    if len(lista)!=len(set(lista)):
        return True
    return False

print(saber_si_hay_duplicados([1,2,3]))
