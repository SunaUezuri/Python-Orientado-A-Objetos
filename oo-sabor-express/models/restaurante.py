#Criando a classe restaurante
class Restaurante:

    #Definindo um método python
    def __init__(self, nome:str, categoria:str):

        #Self é utilizado para indicar que aquele atributo pertence 
        # somente a classe instanciada
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    #Método de exibição
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)