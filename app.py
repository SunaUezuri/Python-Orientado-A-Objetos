#Importando bibliotecas
import os

restaurantes = ['Sushi', 'Sorvete', 'Pizza']

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


def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal.')
    main()


def cadastrar_novo_restaurante():
    os.system('cls')

    print('Cadastro de novos restaurantes\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')

    input('Pressione uma tecla para voltar ao menu principal.')
    main()

def listar_restaurantes():
    os.system('cls')

    print('Listando os restaurantes\n')

    for r in restaurantes:
        print(f'.{r}')

    input('\nPressione uma tecla para voltar ao menu principal.')
    main()

def escolher_opcoes():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativando restaurantes...')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

#Definindo este arquivo como o principal do programa, fazendo com que ele não possa ser importado
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()



if __name__ == '__main__':
    main()