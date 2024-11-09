#Criando a classe restaurante
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizzaria'
restaurante_pizza.categoria = 'Italiano'

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))