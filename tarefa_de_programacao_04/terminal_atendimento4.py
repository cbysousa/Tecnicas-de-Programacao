from tarefa_de_programacao_04.sisbanco import Conta
from tarefa_de_programacao_04.sisbanco import ContaPoupanca
from tarefa_de_programacao_04.sisbanco import ContaEspecial
from tarefa_de_programacao_04.sisbanco import ContaImposto
from tarefa_de_programacao_04.sisbanco import Banco

def terminal():
    opcao = 0
    sisbanco = Banco(0.01, 0.01)
    while opcao != 9:
        print("SisBanco :: Bem-vindo!")
        print("..:::Opções:::..")
        print("0 - CriarConta")
        print("1 - Creditar")
        print("2 - Debitar")
        print("3 - Transferir")
        print("4 - Saldo")
        print("5 - Render Juros")
        print("6 - Render Bonus")
        print("7 - Alterar Taxa de Juros")
        print("8 - Alterar Taxa de Imposto")
        print("9 - Sair")
        opcao = int(input("Digite: "))

        if opcao == 0:
            tipo = input("Digite o tipo de conta a ser criada: (S − Simples | P − Poupança | E − Especial | I - Imposto): ")

            if tipo.lower() == "s":
                numero = input("Digite o número da conta SIMPLES: ")
                conta = Conta(numero)
                sisbanco.cadastrar(conta)
                print("Conta cadastrada com sucesso!")

            elif tipo.lower() == "p":
                numero = input("Digite o número da conta POUPANÇA: ")
                conta = ContaPoupanca(numero)
                sisbanco.cadastrar(conta)
                print("Conta cadastrada com sucesso!")

            elif tipo.lower() == "e":
                numero = input("Digite o número da conta ESPECIAL: ")
                conta = ContaEspecial(numero)
                sisbanco.cadastrar(conta)
                print("Conta cadastrada com sucesso!")

            elif tipo.lower() == "i":
                numero = input("Digite o número da conta IMPOSTO: ")
                conta = ContaImposto(numero)
                sisbanco.cadastrar(conta)
                print("Conta cadastrada com sucesso!")

            else: 
                print("!..::: CONTA INVÁLIDA :::..!")
            
        elif opcao == 1:
            numConta = input("Digite o número da conta que deseja creditar: ")
            valorC = float(input("Digite o valor a ser creditado: "))
            sisbanco.creditarB(numConta, valorC)
            
        elif opcao == 2:
            numConta = input("Digite o número da conta que deseja debitar: ")
            valorC = float(input("Digite o valor a ser debitado: "))
            sisbanco.debitarB(numConta, valorC)
            
        elif opcao == 3:
            contaOrigem = input("Digite o número da conta origem (que irá transferir): ")
            contaDestino = input("Digite o número da conta destino (que irá receber): ")
            valorT = float(input("Digite o valor a ser transferido: "))
            sisbanco.transferir(contaOrigem, contaDestino, valorT)
                     
        elif opcao == 4: 
            numConta = input("Digite o número da conta que deseja consultar o saldo: ")
            sisbanco.saldoB(numConta) 
                
        elif opcao == 5:
            numConta = input("Digite a conta que deseja Render juros: ")
            sisbanco.renderJuros(numConta)

        elif opcao == 6:
            numConta = input("Digite a conta que deseja Render bônus: ")
            sisbanco.renderBonus(numConta)

        elif opcao == 7:
            novaTaxa = float(input("Digite a nova taxa de correção da Poupança: "))
            sisbanco.set_taxa_Poupanca(novaTaxa)

        elif opcao == 8:
            novaTaxa = float(input("Digite a nova taxa de Impostos: "))
            sisbanco.set_taxa_Imposto(novaTaxa)
            
        elif opcao == 9:
            print("SisBanco :: Bye!")
            break

        else:
            print("!..:::NÚMERO INVÁLIDO, DIGITE OUTRO NÚMERO!:::..!")

if __name__ == "__main__":
    terminal()