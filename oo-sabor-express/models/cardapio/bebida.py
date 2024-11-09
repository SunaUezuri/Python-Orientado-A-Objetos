from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome:str, preco:float, tamanho:str):
        super().__init__(nome, preco)
        self._tamanho = tamanho


    def __str__(self):
        return f'{self._nome} | {self._tamanho} | R$ {self._preco:.2f}'