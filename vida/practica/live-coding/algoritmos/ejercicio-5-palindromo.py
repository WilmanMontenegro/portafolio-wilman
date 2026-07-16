
def es_palindrome(palabra):
    palabra_invertida=palabra[::-1]
    if palabra==palabra_invertida:
        return True
    return False


def es_palindrome2(palabra):
    
    j=0
    k=len(palabra)-1

    while (j<=k):
        if palabra[j] != palabra[k]:
            return False
        j+=1
        k-=1

    return True

print(es_palindrome2('reconxnfocer'))
