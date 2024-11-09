x = int(input('Insira a coordenada x: '))
y = int(input('Insira a coordenada y: '))

def define_quadrante(x:int, y:int):
    if x > 0 and y > 0:
        print('Primeiro Quadrante')
    elif x < 0 and y > 0:
        print('Segundo Quadrante')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante')
    elif x > 0 and y < 0:
        print('Quarto Quadrante')
    else:
        print('Eixo Central')

define_quadrante(x, y)