from models.cardapio.item_cardapio import ItemCardapio

class Bebida:
    def __init__(self, nome:str, preco:float, tamanho:str):
        super().__init__(nome, preco)
        self._tamanho = tamanho