import os

restaurantes = [{'nome':'Pizza', 'categoria':'Fast Food', 'ativo':True},
                 {'nome':'Hamburguer', 'categoria':'Fast Food', 'ativo':True},
                 {'nome':'Japonesa', 'categoria':'Fast Food', 'ativo':False},
                 {'nome':'Chinesa', 'categoria':'Fast Food', 'ativo':True},
                 {'nome':'Italiana', 'categoria':'Fast Food', 'ativo':True}]

def exibir_nome_do_programa():
    '''Essa função é utilizada para exibir o nome do programa'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░    
""")

def exibir_opcoes():
    '''Essa função é utilizada para exibir as opções do menu principal'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar Status Restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    '''Essa função é utilizada para voltar ao menu principal'''
    input('Digite uma tecla para continuar: ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é utilizada para exibir um subtitulo'''
    os.system('clear')
    linha = '-' * len(texto)
    print(texto)
    print(linha + '\n')

def opcao_invalida():
    '''Essa função é utilizada para exibir uma mensagem de opção inválida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é utilizada para cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}

    restaurantes.append(dados_do_restaurante)
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é utilizada para ativar ou desativar um restaurante'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_do_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nRestaurante {nome_do_restaurante} ativado com sucesso!' if restaurante['ativo'] else f'\ndRestaurante {nome_do_restaurante} desativado com sucesso!'
            print(mensagem + '\n')
            break

    if not restaurante_encontrado:
        print(f'\nRestaurante {nome_do_restaurante} não encontrado!\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é utilizada para listar todos os restaurantes cadastrados'''
    exibir_subtitulo('Listagem de restaurantes')

    print('Nome do Restaurante'.ljust(22) + ' | ' + 'Categoria'.ljust(20) + ' | ' + 'Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Sim' if restaurante['ativo'] else 'Não'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    print()
    voltar_ao_menu_principal()

def escolher_opcoes():
    '''Essa função é utilizada para escolher as opções do menu principal'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_aplicacao()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_aplicacao():
    '''Essa função é utilizada para finalizar a aplicação'''
    exibir_subtitulo('Obrigado por utilizar o Sabor Express!')

def main():
    '''Essa função é utilizada para executar o programa'''
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main() 