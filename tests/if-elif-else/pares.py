numero = int(input('Insira um número: '))

def calcula_par(number:int):
    if number % 2 == 0:
        print(f'O número {number} é par')
    else:
        print(f'O número {number} é impar')
    
calcula_par(numero)

