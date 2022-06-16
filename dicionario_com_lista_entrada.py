
def realc(s1):
    print('\033[34m_\033[m' * 55)
    print('\033[1;36m', s1, '\033[m')
    print('\033[34m_\033[m' * 55)

print()


realc('\033[7;326m Bem vindo ao Exercicio de Dicionario + Lista \033[m \n\n           \033[7;36mJoão da Silva Barbosa \033[m')

games = {'Nome do jogo:': [], 'Plataforma:': [], 'Ano de lançamento:': []}

for i in range(3):

    #------Nome do Jogo---------
    print('\n\033[7;37m ︽ {}º JOGO ︽ \033[m\n'.format(i+1))
    nome = input('\033[1;32mQual o nome do jogo ?\033[m \n')

    #------Plataforma do Jogo---------=
    print('\n\033[7;37m ︽ PLATAFORMA DO {}º JOGO ︽ \033[m\n'.format(i+1))
    plat = input('\033[1;32mQual a plataforma do jogo ?\033[m\n')

    #------Ano do Jogo---------
    print('\n\033[7;37m ︽ ANO DO {}º JOGO ︽ \033[m\n'.format(i+1))
    ano = input('\033[1;32mQual o ano do jogo ?\033[m\n')
    print('\033[34m_\033[m' * 40)

    #------Processamento---------

    games['Nome do jogo:'].append(nome)
    games['Plataforma:'].append(plat)
    games['Ano de lançamento:'].append(ano)
print('--' * 20)

print(games)
