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
        Restaurante.restaurantes.append(self)

    #Método de exibição de texto
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    #Método da classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(25)} | {r._categoria.ljust(25)} | {r.ativo}')

    #Pega um atributo e modifica como aquele atributo é lido
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    #Método dos atributos
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

Restaurante.listar_restaurantes()