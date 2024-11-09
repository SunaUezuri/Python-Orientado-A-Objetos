from models.restaurante import Restaurante


restaurante_praca = Restaurante('praça', 'gourmet')

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Suna', 7)
restaurante_praca.receber_avaliacao('Ellen', 5.5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()