# -*- coding: utf-8 -*-

def main():
   temps = [21,24,24,22,20,23,24]
   promedio = calculo_temps(temps)
   print ('La temperatura promedio es: {}'.format(promedio))

def calculo_temps(temps):
    suma_de_temps = 0;

    for temp in temps:
        suma_de_temps+= float(temp)
    
    return suma_de_temps / len(temps)

if __name__ == "__main__":
    main()