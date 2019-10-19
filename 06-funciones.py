# -*- coding: utf-8 -*-

import turtle

def main():
    # Abrimos la ventana
    window = turtle.Screen()
    # Generamos una tortuga
    tortuga = turtle.Turtle()
    # Hacemos un cuadrado
    hacer_cuadrado(tortuga)
    tortuga.mainloop()

def hacer_cuadrado(tortuga):
    #Pregunta el tamaño
    length = int(input('largo: '))
    #Generamos 4 veces la instruccion hacer_linea_dar_vueltas
    for i in range(4):
        hacer_linea_dar_vueltas(tortuga, length)

def hacer_linea_dar_vueltas(tortuga, length):
    tortuga.forward(length)
    tortuga.left(90)

if __name__ == '__main__':
    main()