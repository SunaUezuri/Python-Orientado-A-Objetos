from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de melância', 5.0, 'Grande')

prato_feijoada = Prato('Feijoada', 30.0, 'Típica feijoada nordestina')



def main():
    print(bebida_suco)
    print(prato_feijoada)

if __name__ == '__main__':
    main()