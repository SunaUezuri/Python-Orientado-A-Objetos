from models.cardapio.item_cardapio import ItemCardapio

#Classe com herança aplicada no PYTHON
class Prato(ItemCardapio):
    def __init__(self, nome:str, preco:float, descricao:str):
        super().__init__(nome, preco)
        self.descricao = descricao


    def __str__(self):
        return f"Nome: {self._nome} | Preço: {self._preco:.2f} | Descrição: {self._descricao}"