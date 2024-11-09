#Importando bibliotecas
import os

restaurantes = [{'nome' : 'Bazzinga', 'categoria': 'chinesa', 'ativo': False}, 
                {'nome': 'PizzaHurt', 'categoria': 'francesa', 'ativo': True},
                {'nome': 'DonaldsMc', 'categoria': 'fast food', 'ativo': False}
                ]

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

def voltar_menu_principal():
    input('\nPressione uma tecla para voltar ao menu principal.')
    main()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


#Definindo uma função
def finalizar_app():
    exibir_subtitulo('Finalizando programa.')


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def exibir_subtitulo(texto:str):
    os.system('cls')
    print(texto)
    print('\n')


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Insira a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')

    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    

    for r in restaurantes:
        nome_restaurante = r['nome']
        categoria = r['categoria']
        ativo = r['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_menu_principal()

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