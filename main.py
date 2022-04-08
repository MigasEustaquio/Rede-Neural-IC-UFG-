import random

# [N1, N2, output]
BACH = [0, 0, 0]
BEETHOVEN = [0, 1, 0]
EINSTEIN = [1, 0, 1]
KEPLER = [1, 1, 1]

nomes = ['BACH', 'BEETHOVEN', 'EINSTEIN', 'KEPLER']
database = [BACH, BEETHOVEN, EINSTEIN, KEPLER]
saida_eperada = [BACH[2], BEETHOVEN[2], EINSTEIN[2], KEPLER[2]]

# TESTE COM INDIVÍDUOS EM ORDENS DIFERENTES

# nomes = ['BACH', 'EINSTEIN', 'BEETHOVEN', 'KEPLER']
# database = [BACH, EINSTEIN, BEETHOVEN, KEPLER]
# saida_eperada = [BACH[2], EINSTEIN[2], BEETHOVEN[2], KEPLER[2]]

Wb = 0
W1 = 0 
W2 = 0
Bias = 1
taxa_aprendizagem = 1
valor_erro = 0

N1 = 0
N2 = 0

testes_bem_sucedidos=0
numero_tentativa=1
while True:
    print(str(numero_tentativa) + '° tentativa...\n')

    teste = random.randint(0,3)

    while True:

        saida = (Bias*Wb)+(database[teste][0]*W1)+(database[teste][1]*W2)
        if saida>0: saida=1

        print('Fazendo teste para o indivídio: ' + nomes[teste] + '...')
        if saida == saida_eperada[teste]:
            print('Teste bem sucedido!')
            teste +=1
            if teste > 3: teste = 0
            testes_bem_sucedidos+=1
        else:
            print('Teste mal sucedido. Alterando os valores do pesos...')
            print('------------------------------\n')
            numero_tentativa+=1
            testes_bem_sucedidos=0
            N1 = database[teste][0]
            N2 = database[teste][1]
            valor_erro = saida_eperada[teste]-saida
            break

        if testes_bem_sucedidos == 4: break

    if testes_bem_sucedidos == 4:
        print('\nRede treinada com sucesso!')
        print('Pesos finais alcançados:\nWb = ' + str(Wb) + ' W1 = ' + str(W1) + '  W2 = ' + str(W2) + '\n')
        break

    Wb = Wb + (valor_erro * taxa_aprendizagem * 1)
    W1 = W1 + (valor_erro * taxa_aprendizagem * N1)
    W2 = W2 + (valor_erro * taxa_aprendizagem * N2)