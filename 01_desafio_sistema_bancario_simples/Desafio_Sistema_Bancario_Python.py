menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        
    elif opcao == 's':
        valor = float(input('Informe o valor a sacar: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print('Operação não realizada. Saldo insuficiente')
        elif excedeu_limite:
            print('Operação não realizada. Valor do saque excede o limite')
        elif excedeu_saques:
            print('Operação não realizada. Excedeu o limite diário de saques')
        else:
            print('Operação falhou. O valor informado é inválido.')
            
    elif opcao == 'e':
        print('\n******** EXTRATO ********')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print('*' * 25)
        print(f'\nSaldo: R$ {saldo:.2f}')
       
    elif opcao == 'q':
        break
    
    else:
        print('Transação inválida, por favor selecione a opção desejada.')
