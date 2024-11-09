from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de melância', 5.0, 'Grande')

prato_feijoada = Prato('Feijoada', 30.0, 'Típica feijoada nordestina')
bebida_suco.aplicar_desconto()
prato_feijoada.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_feijoada)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()