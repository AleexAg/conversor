def conversor(p_dolar, moneda):
    cantidad_m = float(input(f'Ingrese la cantidad de {moneda}: '))

    dolar = cantidad_m / p_dolar
    dolar = round(dolar, 2)

    print(f'Es un total de ${dolar} USD')


def principal():
    op = 0
    while op != 4:
        print('-' * 35)
        print('|  CONVERSOR DE MONEDA A DOLAR  |')
        print('1 - PESOS ARGENTINOS \n'
                '2 - PESOS MEXICANOS \n'
                '3 - PESOS COLOMBIANOS\n'
                '4 - SALIR ')
        print('-' * 35)
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            conversor(370, 'Pesos Argentinos')
        elif op == 2:
            conversor(18.77, 'Pesos Mexicanos')
        elif op == 3:
            conversor(4690, 'Pesos colombianos')
        elif op <= 0 or op > 4:
            print('No es una opcion valida!')



if __name__ == '__main__':
    principal()
