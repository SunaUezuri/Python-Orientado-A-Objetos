#Criando a classe restaurante
class Restaurante:

    restaurantes = []

    #Definindo um método python
    def __init__(self, nome:str, categoria:str):

        #Self é utilizado para indicar que aquele atributo pertence 
        # somente a classe instanciada
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    #Método de exibição de texto
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for r in Restaurante.restaurantes:
            print(f'{r.nome} | {r.categoria} | {r.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

Restaurante.listar_restaurantes()