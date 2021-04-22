from random import randint
from time import sleep

continuar = 'Ss'
while continuar in 'Ss':
    print('\033[1;32mVamos jogar. Exemplo: 1d20 ou 5d10\033[m')
    opc = input()
    qntDados = int(opc[:1])
    valorDado = int(opc[2:])
    if qntDados > 10 or valorDado not in [4,6,8,10,12,20,100]:
        print('\033[1;31mErro! Quantidade da dados ou valor dos dados é inválido!\033[m')
    elif valorDado in [4,6,8,10,12,20,100]:
        dado = 1
        for l in range(qntDados):
            sleep(0.5)
            print(f'Valor do dado 0{dado}: {randint(1, valorDado)}')
            dado = dado + 1
        continuar = str(input('Jogar novamente? S ou N?'))
sleep(1)
print('Até! o/')