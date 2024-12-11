from sisbanco import Conta, Banco

def terminal():
    sisbanco = Banco()
    while(True):
        print('Sisbanco::Bem-Vindo!')
        print('.:: Opcoes ::.')
        print('[0] - Criar Conta')
        print('[1] - Creditar')
        print('[2] - Debitar')
        print('[3] - Transferir')
        print('[4] - Saldo')
        print('[5] - Sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 0:
            numero_conta = input("Digite o número da conta: ")
            conta = Conta(numero_conta)
            sisbanco.cadastrar(conta)
            print("Conta cadastrada com Sucesso")

        elif opcao == 1:
            numero_conta = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a ser Creditado: R$"))
            sisbanco.creditar(numero_conta, valor)
            print(f"O valor de R${valor} foi creditado com Sucesso em sua conta!")

        elif opcao == 2:
            numero_conta = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a ser Debitado: "))
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
            print("SisBanco :: Bye!")
            break
        
        else:
            print('Opção inválida!')


if __name__ == "__main__":
    terminal()