# -*- coding: utf-8 -*-

def run():
    print('C A L C U L A D O R A')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')

    monto = float(input('pesos mexicanos: '))
    resultado = convertir(monto)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(monto, resultado))
    print('')

def convertir(monto):
    tipo_cambio = 145.97
    return tipo_cambio * monto

if __name__ == '__main__':
    run()