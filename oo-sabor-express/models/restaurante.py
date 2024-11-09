from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio

#Criando a classe restaurante
class Restaurante:

    restaurantes = []

    #Definindo um método python
    def __init__(self, nome:str, categoria:str):

        #Self é utilizado para indicar que aquele atributo pertence 
        # somente a classe instanciada
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    #Método de exibição de texto
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    #Método da classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(25)} | {r._categoria.ljust(25)} | {str(r.media_avaliacoes).ljust(25)} | {r.ativo}')

    #Pega um atributo e modifica como aquele atributo é lido
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    #Método dos atributos
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente:str, nota:float):

        if nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print('Nota inválida. A nota deve ser um número entre 1 e 5.')

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        
        soma_notas = sum(av._nota for av in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}: \n')

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                print(f'{i}. {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}')
            else:
                print(f'{i}. {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}')
