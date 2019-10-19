# -*- coding: utf-8 -*-

def factorial(numero):
    if(numero==0):
        return 1

    return numero * factorial(numero-1)

if __name__ == "__main__":
    numero = int(input('Escribe un número: '))
    result = factorial(numero)
    print(result)