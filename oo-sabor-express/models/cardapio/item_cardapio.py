from abc import ABC, abstractmethod as abstract

class ItemCardapio(ABC):
    def __init__(self, nome:str, preco:float):
        self._nome = nome
        self._preco = preco

    @abstract
    def aplicar_desconto(self):
        pass