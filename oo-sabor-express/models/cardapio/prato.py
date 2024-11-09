from models.cardapio.item_cardapio import ItemCardapio

#Classe com herança aplicada no PYTHON
class Prato(ItemCardapio):
    def __init__(self, nome:str, preco:float, descricao:str):
        super().__init__(nome, preco)
        self._descricao = descricao