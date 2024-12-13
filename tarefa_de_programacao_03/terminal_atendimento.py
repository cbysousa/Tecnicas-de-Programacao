from sisbanco import Conta, Banco, ContaEspecial, ContaPoupanca

def terminal():
    opcao = 0
    sisbanco = Banco(0.01)
    while opcao != 8:
        print('Sisbanco::Bem-Vindo!')
        print('.:: Opcoes ::.')
        print('[0] - Cadastrar Conta')
        print('[1] - Creditar')
        print('[2] - Debitar')
        print('[3] - Transferir')
        print('[4] - Consultar Saldo')
        print('[5] - Render Juros')
        print('[6] - Render Bônus')
        print('[7] - Alterar taxa de juros')
        print('[5] - Sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 0:
            tipo_conta = input('Digite o tipo de conta a ser criada: S - Simples | P - Poupança | E - Especial ').lower()
            if tipo_conta == 's' or 'simples':
                numero_conta = input("Digite o número da conta: ")
                conta = Conta(numero_conta)
                sisbanco.cadastrar(conta)
                print('Conta cadastrada com sucesso!')
            elif tipo_conta == 'p' or 'poupança':
                numero_conta = input('Digite o número da conta: ')
                conta = ContaPoupanca(numero_conta)
                sisbanco.cadastrar(conta)
                print('Conta criada com sucesso!')
            elif tipo_conta == 'e' or 'especial':
                numero_conta = input('Digite o número da conta: ')
                conta= ContaEspecial(numero_conta)
                sisbanco.cadastrar(conta)
                print('Conta cadastrada com sucesso!')
            else:
                print('Opção inválida!')

        elif opcao == 1:
            valor = float(input("Digite o valor a ser Creditado: R$"))
            sisbanco.creditar(numero_conta, valor)
            print(f"O valor de R${valor} foi creditado com sucesso em sua conta!")

        elif opcao == 2:
            numero_conta = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a ser debitado: "))
            sisbanco.debitar(numero_conta, valor)
            print(f"O valor de R${valor} foi debitado com Sucesso em sua conta!")

        elif opcao == 3:
            numero_conta = input("Digite o número da conta de origem: ")
            conta_destino = input("Digite o número da conta destino: ")
            valor = float(input("Digite a quantia a ser transferida: R$ "))
            sisbanco.transferir(numero_conta, conta_destino, valor)

        elif opcao == 4:
            numero_conta = input("Informe o número da conta: ")
            sisbanco.saldo(numero_conta)

        elif opcao == 5:
            numero_conta = input('Digite o número da sua conta poupança: ')
            sisbanco.render_juros(numero_conta)
            print('Sua conta poupança começou a render!')

        elif opcao == 6:
            numero_conta = input('Digite o número da sua conta especial: ')
            sisbanco.render_bonus(numero_conta)
            print('Sua conta especial começou a render!')
        
        elif opcao == 7:
            taxa = float(input('informe o novo valor da taxa: '))
            sisbanco.set_taxa(taxa)
            print('Taxa atualizada!')

        elif opcao == 8:
            print("SisBanco :: Bye!")
        
        else:
            print('Opção inválida!')


if __name__ == "__main__":
    terminal()