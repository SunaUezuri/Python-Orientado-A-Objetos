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
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


#Definindo uma função
def finalizar_app():
    exibir_subtitulo('Finalizando programa.')


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def exibir_subtitulo(texto:str):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
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

    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'}')
    for r in restaurantes:
        nome_restaurante = r['nome']
        categoria = r['categoria']
        ativo = 'ativado' if r['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()


def alternar_estado_do_restaurante():
    exibir_subtitulo('Ativando/desativando restaurantes')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')

    restaurante_encontrado = False

    for r in restaurantes:
        if nome_restaurante == r['nome']:
            restaurante_encontrado = True
            r['ativo'] = not r['ativo']
            if r['ativo']:
                mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' 
            else:
                mensagem = f'O restaurante {nome_restaurante} foi desativado com sucesso'

            print(mensagem)
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado')

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
                alternar_estado_do_restaurante()
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