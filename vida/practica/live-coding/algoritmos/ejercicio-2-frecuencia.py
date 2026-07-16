


def contar_letras(palabra):

    conteo = {}
    for letra in palabra:
        if letra in conteo:
            conteo[letra]+=1
        else:
             conteo[letra]=1
    return conteo
        
print(contar_letras("ammorr"))

