# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def palabra_aleatoria():
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def mostrar_tablero(palabra_oculta, intentos):
    print(IMAGES[intentos])
    print('')
    print(palabra_oculta)
    print('--- * --- * --- * --- * ---')

def run():
    palabra =  palabra_aleatoria()
    palabra_oculta = ['-'] * len(palabra)
    intentos = 0
    
    while True:
        mostrar_tablero(palabra_oculta, intentos)
        pedir_letra = str(input('Escoge una letra: '))
        indices_letras = []
        for i in range(len(palabra)):
            if(palabra[i] == pedir_letra):
                indices_letras.append(i)

        if len(indices_letras)==0:
            intentos+=1
            if intentos==7:
                mostrar_tablero(palabra_oculta, intentos)
                print('')
                print('Lo sentimos, has perdido, la palabra era {}'.format(palabra))
                break
        else:
            for i in indices_letras:
                palabra_oculta[i] = pedir_letra

            indices_letras = []
        
        try:
            palabra_oculta.index('-')
        except ValueError:
            print('')
            print('¡Congratulations!, Ganaste, la palabra es {}'.format(palabra))
            break

if __name__ == '__main__':
    print('--- A H O R C A D O S ---')
    run()