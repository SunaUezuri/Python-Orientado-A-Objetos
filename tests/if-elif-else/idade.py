def classifica_idade(idade:int):
    if idade >= 0 and idade <= 12:
        print("Criança")
    elif idade >= 13 and idade <= 18:
        print("Adolescente")
    else:
        print("Adulto")

idade = int(input("Insira sua idade: "))

classifica_idade(idade)