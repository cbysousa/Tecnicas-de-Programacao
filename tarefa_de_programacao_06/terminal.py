from sisbanco import *

def terminal():
   sisbanco = Banco()
   while(True):
      print("SisBanco::Bem-Vindo!")
      print(".::Opcoes::.")
      print("[0] Cadastrar Conta")
      print("[1] Creditar")
      print("[2] Debitar")
      print("[3] Transferir")
      print("[4] Consultar Saldo")
      print("[5] Render Juros")
      print("[6] Render Bonus")
      print("[7] Alterar Taxa_Juros")      
      print("[8] Alterar Taxa_Imposto")
      print("[9] Sair")
      opcao = input("Digite:")
      
      try:
         opcao = int(opcao)
         if opcao == 0:
            tipo_conta = input('Escolha o tipo de conta a ser criada' + 
                                    '(S - Simples | P - Poupança | E - Especial | I - Imposto): ').lower().strip()
            numero_conta = input('Número da conta a ser criada: ')
            if tipo_conta == 's':
               conta = Conta(numero_conta)
            elif tipo_conta == 'p':
               conta = ContaPoupanca(numero_conta)
            elif tipo_conta == 'e':
               conta = ContaEspecial(numero_conta)
            elif tipo_conta == 'i':
               conta = ContaImposto(numero_conta)
            else:
               print("Insira um tipo válido.")
               print("")
               continue
            sisbanco.cadastrar(conta)
            #qual tipo de conta a ser criada: 
            #S - Simples  | P - Poupanca | E - Especial | I - Imposto
            #solicite o numero da conta a ser criada
            #instancie uma conta do tipo selecionado com esse numero
            #cadastre a conta no sisbanco

         elif opcao == 1:
            numero_conta = input('Número da conta que deseja creditar: ')
            valor_credito = float(input('Valor a ser creditado: '))
            sisbanco.creditar(numero_conta, valor_credito)
            #solicite o numero da conta alvo
            #solicite o valor a ser creditado
            #realize a operacao de credito no sisbanco

         elif opcao == 2:
            numero_conta = input('Número da conta que deseja debitar: ')
            valor_debito = float(input('Valor a ser debitado: '))
            sisbanco.debitar(numero_conta, valor_debito)
            #solicite o numero da conta alvo
            #solicite o valor a ser debitado
            #realize a operacao de debito no sisbanco

         elif opcao == 3:
            origem = input('Conta de origem: ')
            destino = input('Conta de destino: ')
            valor = float(input('Valor de transferência: '))
            sisbanco.transferir(origem, destino, valor)
            #solicite o numero da conta origem
            #solicite o numero da conta destino
            #solicite o valor a ser transferido
            #realize a operacao de transferencia no sisbanco

         elif opcao == 4:
            numero_conta = input('Número da conta que deseja conferir: ')
            saldo = sisbanco.saldo(numero_conta)
            print(f"Saldo: {saldo}")
            #solicite o numero da conta alvo
            #realize a operacao de obtencao de saldo no sisbanco
            #exiba o saldo na tela
         
         elif opcao == 5:
            numero_conta = input('Número da conta: ')
            sisbanco.render_juros(numero_conta) 
            #solicite o numero da conta alvo
            #realize a operacao correcao da poupanca no sisbanco
         
         elif opcao == 6:
            numero_conta = input('Número da conta: ')
            sisbanco.render_bonus(numero_conta)
            #solicite o numero da conta alvo
            #realize a operacao conversao/rendimento de bonus no sisbanco
         
         elif opcao == 7:
            taxa = input('Nova taxa: ')
            sisbanco.set_taxa_poupanca(int(taxa))
            #solicite a nova taxa de correcao da poupanca
            #realize a operacao de alteracao da taxa no sisbanco

         elif opcao == 8:
            taxa = input('Nova taxa: ')
            sisbanco.set_taxa_imposto(int(taxa))
            #solicite a nova taxa de imposto
            #realize a operacao de alteracao da taxa no sisbanco
            
         elif opcao == 9:
            print("SisBanco::Bye!")
            break

      except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
      except (VIException, SIException, TJIException, CIException, CEException) as e:
            e.print_mensagem_erro()
      except Exception as e:
            print(f"Erro inesperado: {e}")
      finally:
            print("")

if __name__ == "__main__":
   terminal()