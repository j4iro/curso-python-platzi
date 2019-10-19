# -*- coding: utf-8 -*-
import random

def main():
    numero_encontrado = False;
    numero_random = random.randint(0, 20)

    while not numero_encontrado:
        numero = int(input('Escribe un numero: '))
        if numero==numero_random:
            print('Felicidades, encontraste el numero')
            numero_encontrado = True
        elif numero > numero_random:
            print('El número es más pequeño')
        else:
            print('El número es más grande')

if __name__ == "__main__":
    main()