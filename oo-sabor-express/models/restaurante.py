#Criando a classe restaurante
class Restaurante:

    #Definindo um método python
    def __init__(self, nome:str, categoria:str):

        #Self é utilizado para indicar que aquele atributo pertence 
        # somente a classe instanciada
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))