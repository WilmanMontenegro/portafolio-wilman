def es_anagrama(palabra1, palabra2):

    if len(palabra1)!= len(palabra2):
        return False

    for letra in palabra1:
        if palabra1.count(letra) != palabra2.count(letra):
            return False
    
    return True

print(es_anagrama("aba","baa"))