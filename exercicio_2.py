# Suponha que você é colecionador de jogos de videogame. Escreva um algoritmo que permita
# cadastrar esses jogos informando o nome e a qual videogame ele pertente.
# Para isso, crie um menu de opções contendo:
# Cadastrar novo item, listar tudo que foi cadastrado e sair
# Crie uma função para cada item do menu
# Armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados



print()

def realce(s1):


    print('\033[34m_\033[m' * 45)
    print('\033[1;36m               ', s1, '\033[m')
    print('\033[34m_\033[m' * 45)


def valida_ex2(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


# Função para criar arquivo
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')  # w= Escrita , t= Texto , += Criação
        a.close()
    except:
        print('\033[1;31mErro na criação do arquivo\033[m')
    else:
        print('\033[1;37mArquivo {} foi criado com sucesso:\033[m '.format(nomeArquivo))


# Função verifica se o arquivo existe.
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')  # Tentativa de abrir o arquivo
        a.close()  # Tentativa de fechar o arquivo
    except FileNotFoundError:  # Se a tentativa falhar
        return False
    else:
        return True

# Função para Listar jogos e VideoGame
def listarArquivo(nomeArquivo):

    try:
        a = open(nomeArquivo,'rt')
    except:
        print('\033[1;31mErro ao ler o arquivo\033[m')
    else:
        print(a.read())
    finally:
        a.close()



# Função para cadastrar jogo e VideoGame
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    """
    Função para cadastrar os jogos e videogame no arquivo
    :param nomeArquivo:    Arquivo já  criado antes
    :param nomeJogo:       Jogo escolhido pelo usuario
    :param nomeVideogame:  Jogo escolhido pelo usuario
    :return:
    """
    try:
        # Aqui, tentativa de abrir o arquivo mas mantendo o que já está salvo
        a = open(nomeArquivo, 'at')  # A = Abrir para escrita e manter o salvo, t= Texto

    # Caso ocorra um erro.
    except:
        # Aparecerá isso:
        print('\033[1;31mErro ao abrir o arquivo\033[m')
    # Caso não ocorra nenhum erro.
    else:
        # Comando write para escrever o nome do jogo e videogame
        a.write(' {} ; {} \n'.format(nomeJogo, nomeVideogame))
    # Ocorrendo erro ou não...
    finally:
        # Comando para fechar o arquivo
        a.close()



# Programa principal

arquivo = 'games.txt'

# Retorno da função que verifica se o arquivo existe
if existeArquivo(arquivo):  # Se retornar TRUE
    print('\033[1;37mArquivo localizado no computador\033[m')
else:  # Se RETORNAR FALSE
    print('\033[1;31mArquivo inexistente\033[m')
    criarArquivo(arquivo)

# Menu com loop até opção de sair
while True:
    realce(' MENU')
    print('\033[1;32m1 - Cadastrar novo item')
    print('\033[1;33m2 - Listar cadastro')
    print('\033[1;31m3 - Sair\033[m')
    try:
        op = valida_ex2('\n\033[7;37mEscolha a opção desejada: >> \033[m ', 1, 3)

        print('\033[37m_\033[m' * 45)
        if op == 1:
            print('\n\033[7;32mOpção de cadastrar novo item selecionado\033[m')
            nomeJogo = input('\n\033[1;32mNome do jogo: >> \033[m')
            nomeVideogame = input('\033[1;32mNome do VideoGame: >> \033[m')
            print('\n\033[7;35mCADASTRADO COM SUCESSO !\033[m')
            # Função para cada item
            cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
        elif op == 2:
            print('\n\033[7;33mOpção de listar novo item selecionada\033[m')
            print()
            listarArquivo(arquivo)
        elif op == 3:
            print('\033[7;31mEncerrando o programa...\033[m')
            break

    except ValueError:
        print('\n\033[7;31mERRO ! Você digitou um caractere no lugar de número\033[m')
        print()
