import random
import os
print('dkjf')

#NOMES
nomes = ['ALEXANDRE RODRIGUES FIGUEIREDO',
         'CAMILA FRAGA CORREA DOS ANJOS',
         'AILTON TEIXEIRA DA SILVA',
         'FELIPE APARECIDO OLIVEIRA',
         'RODOLPHO CESAR DE OLIVEIRA',
         'PEDRO HENRIQUE FIDALGO',
         'RICARDO LUIZ PEREIRA SANTANA',
         'FABIO SILVA SANTOS',
         'KESSIO CAVALCANTE DE AMORIM',
         'EVERTON MARTINS',
         'ERICSON CALLEGARI OLIVEIRA',
         'MARCO ANTONIO DE OLIVEIRA GRAGNANO',
         'CARLOS EDUARDO BASTOS RIBEIRO',
         'EDMARILES REVOREDO RODRIGUES',
         'CARLO GRAF RUECKER',
         'EDGAR HEMETERIO',
         'Diego Fabris Martine',
         'MARCELO JOSE GONCALVES LINS FILHO',
         'ELIAS PEREIRA JUNIOR',
         'FERNANDO DE JESUS MONTEIRO'
         ]

#emails
emails = ['16@EMAIL.COM',
          '37@EMAIL.COM',
          '30@EMAIL.COM',
          '96@EMAIL.COM',
          '65@EMAIL.COM',
          '56@EMAIL.COM'
          ]

#telefone
telefone_prefix = random.randint(10, 69)
telefone1 = random.randint(50, 55)
telefone2 = random.randint(1, 99)
telefone_seq = random.randint(1000, 9999)

# ESTADO
estado = ['SP', 'RJ', 'PA', 'RO']

#ESCOLHAS
escolha_continuar = 'k'
# escolha_nome = 'initi'
# escolha_email = '@initi'
# escolha_num_tel = 000
# escolha_estado = 'estado_initi'
# escolha_opcao = '0'
# escolha_salvar = 'n'

#layout

while escolha_continuar != 'n':
    print('=================================================================')

    print('=================BEM VINDO AO GERADOR DE DADOS===================')

    print('=================================================================')

    print('''-Escolha uma opção abaixo para gerar as informações aleatoriamente''')
    print('=================================================================')

    print('''[1]-Nome
             [2]-Email
             [3]-Telefone
             [4]-Estado
                    ''')
    print('=================================================================')
    print('digite o numero da opção')
    escolha_opcao = list(str(input()))

    print('=================================================================')

    print('Gostaria de salvar os dados em arquivo Txt (s/n)')

    print('=================================================================')

    escolha_salvar = str(input())

# Tratando escolhas
    if '1' in escolha_opcao:
        dado1 = random.choice(nomes)
    else:
        dado1=''    
        print(dado1)
    if '2' in escolha_opcao:
        dado2 = random.choice(emails)
    else:
        dado2=''    
        print(dado2)
    if '3' in escolha_opcao:
        dado3 = (f'0{telefone_prefix}-{telefone1}{telefone2}-{telefone_seq}')
    else:
        dado3=''    
        print(dado3)
    if '4' in escolha_opcao:
        dado4 = random.choice(estado)
    else:
        dado4 =''
        print(dado4)    

    print(dado1)
    print(dado2)
    print(dado3)
    print(dado4)

#gerando arquivo
    if escolha_salvar == 's':
        
        with open('base2.txt', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(dado1 + os.linesep + dado2+os.linesep+dado3+os.linesep+dado4)
        print('dados gravados com sucesso')
    else:
     print('arquivos não gravados')

    print('=================================================================')

    print('deseja continuar (s/n)')

    escolha_continuar = str(input())