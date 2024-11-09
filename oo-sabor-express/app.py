from models.restaurante import Restaurante


restaurante_praca = Restaurante('praça', 'gourmet')

restaurante_praca.receber_avaliacao('Gui', 4.2)
restaurante_praca.receber_avaliacao('Suna', 3.7)
restaurante_praca.receber_avaliacao('Ellen', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()