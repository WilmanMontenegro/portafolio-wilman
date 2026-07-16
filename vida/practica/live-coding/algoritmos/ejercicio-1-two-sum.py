
def sum_9(lista,target):

    for j, valor in enumerate(lista):
        for k,valor2 in enumerate(lista):
            if j!=k: #que no sea la misma posicion
                if valor + valor2 == target:
                    return [j,k];



print(sum_9([2, 7, 11, 15],9))