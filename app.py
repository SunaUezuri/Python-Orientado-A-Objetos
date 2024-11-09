#Importando bibliotecas
import os

#Podemos usar triplas aspas para manter uma quebra de linha ao invés do "\n"
def exibir_nome_programa():
    print(''' 

░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


#Definindo uma função
def finalizar_app():
    #Limpando o console utiizando a biblioteca os
    os.system('cls')
    print('Finalizando programa\n')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))

    match opcao_escolhida:
        case 1:
            print('Cadastro de restaurantes...')
        case 2:
            print('Listando restaurantes...')
        case 3:
            print('Ativando restaurantes...')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida. Tente novamente.')
            escolher_opcoes()


#Definindo este arquivo como o principal do programa, fazendo com que ele não possa ser importado
def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()