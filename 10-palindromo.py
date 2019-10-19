# -*- coding: utf-8 -*-

def palindromo(palabra):
    letras_reves = []

    for letra in palabra:
        # print(letra + ' ')
        letras_reves.insert(0, letra)
    
    palabra_reves = ''.join(letras_reves)
    if palabra_reves==palabra:
        return True
    else:
        return False

def palindromo2(palabra):
    palabra_reves = palabra[::-1]
    if palabra_reves==palabra:
        return True
    else:
        return False

if __name__ == "__main__":
    palabra = str(input("Escribe una palabra: "))
    result = palindromo2(palabra)
    # print(result)
    
    if result is True:
        print('{} si es un palindromo'.format(palabra))
    else:
        print('{} NO es un palindromo'.format(palabra))
        pass
    