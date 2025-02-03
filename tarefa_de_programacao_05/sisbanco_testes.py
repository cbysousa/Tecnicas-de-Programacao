import unittest

from sisbanco_bugs import Conta, Banco, ContaAbstrata, ContaEspecial, ContaImposto, ContaPoupanca

class TestConta(unittest.TestCase):
    def test_creditar(self):
        conta = Conta('1234-X')
        conta.creditar(10.00)
        self.assertEqual(conta.get_saldo(), 10.00, "Erro no teste de creditar")

    def test_debitar(self):
        conta = Conta('1234-X')
        conta.debitar(20)
        self.assertEqual(conta.get_saldo(), -20, 'Erro no teste de debitar')

    def test_numero(self):
        conta = Conta('12345')
        teste = conta.get_numero()
        self.assertEqual(teste, '12345')

    def test_saldo(self):
        conta = Conta('12345')
        saldo = conta.get_saldo()
        self.assertEqual(saldo, 0)
    
    def test_saldo_inicial(self):
        conta = Conta('12345')
        self.assertEqual(conta.get_saldo(), 0.0, "Saldo inicial incorreto.") #BUG 1

    def test_creditar_negativo(self): # BUG 2
        conta = Conta('1234-X')
        conta.creditar(10.00)
        self.assertEqual(conta.get_saldo(), 10.00, "Erro ao creditar valor positivo")

    def test_debitar_positivo(self): # BUG 3
        conta = Conta('1234-X')
        conta.debitar(20)
        self.assertEqual(conta.get_saldo(), -20.0, 'Erro ao debitar valor positivo')

class TestContaPoupanca(unittest.TestCase):
    def test_render_juros(self):
        conta = ContaPoupanca('54321')
        conta.creditar(50)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 55)

    def test_render_juros_divisao(self): # BUG 4
        conta = ContaPoupanca('54321')
        conta.creditar(50)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 550.0, "Erro no cálculo do rendimento dos juros (divisão)")

class TestContaEspecial(unittest.TestCase):
    def test_render_bonus(self):
        conta = ContaEspecial('1234')
        conta.creditar(valor=100)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101.0)

    def test_creditar_especial(self):
        conta = ContaEspecial('40028922')
        conta.creditar(200)
        self.assertEqual(conta.get_saldo(), 200)
        self.assertEqual(conta._ContaEspecial__bonus, 2.0)
    
    def test_render_bonus_sem_bonus(self): # BUG 5
        conta = ContaEspecial('1234')
        conta.creditar(valor=100)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101, "Bonus não creditado")

    def test_creditar_especial(self): # BUG 6
        conta = ContaEspecial('40028922')
        conta.creditar(200)
        self.assertEqual(conta.get_saldo(), 200.0)
        self.assertEqual(conta._ContaEspecial__bonus, 2.0)

class TestContaImposto(unittest.TestCase):
    def test_debitar(self):
        conta = ContaImposto('1234')
        conta.creditar(100)
        conta.debitar(10)
        self.assertAlmostEqual(conta.get_saldo(), 89.99, places=2)

    def test_get_taxa(self):
        conta = ContaImposto('1234')
        self.assertEqual(conta.get_taxa(), 0.001)

    def test_set_taxa(self):
        conta = ContaImposto('1234')
        conta.set_taxa(0.005)
        self.assertEqual(conta.get_taxa(), 0.005)

    def test_debitar_imposto_subtracao(self): # BUG 7
        conta = ContaImposto('1234')
        conta.creditar(100)
        conta.debitar(10)
        self.assertAlmostEqual(conta.get_saldo(), 89.99, places=2, msg="Erro no cálculo do débito com imposto (subtração)")

class TestBanco(unittest.TestCase):
    def test_casdastrar(self):
        banco = Banco()
        conta = Conta('1234')
        banco.cadastrar(conta)
        self.assertEqual(banco.procurar('1234'), conta)

    def test_procurar(self):
        banco = Banco()
        conta = Conta('1234')
        banco.cadastrar(conta)
        self.assertEqual(banco.procurar('1234'), conta)
        self.assertIsNone(banco.procurar('5678'))

    def test_creditar(self):
        banco = Banco()
        conta = Conta('1234')
        banco.cadastrar(conta)
        banco.creditar('1234', 100)
        self.assertEqual(conta.get_saldo(), 100)

    def test_debitar(self):
        banco = Banco()
        conta = Conta('1234')
        banco.cadastrar(conta)
        banco.creditar('1234', 100)
        banco.debitar('1234', 50)
        self.assertEqual(conta.get_saldo(), 50)

    def test_saldo(self):
        banco = Banco()
        conta = Conta('1234')
        banco.cadastrar(conta)
        banco.creditar('1234', 100)
        self.assertEqual(banco.saldo('1234'), 100)

    def test_transferir(self):
        banco = Banco()
        conta_origem = Conta('1234')
        conta_destino = Conta('5678')
        banco.cadastrar(conta_origem)
        banco.cadastrar(conta_destino)
        banco.creditar('1234', 100)
        banco.transferir('1234', '5678', 50)
        self.assertEqual(conta_origem.get_saldo(), 50)
        self.assertEqual(conta_destino.get_saldo(), 50)

    def test_get_taxa_poupanca(self):
        banco = Banco(taxa_poupanca=0.01)
        self.assertEqual(banco.get_taxa_poupanca(), 0.01)

    def test_set_taxa_poupanca(self):
        banco = Banco()
        banco.set_taxa_poupanca(0.02)
        self.assertEqual(banco.get_taxa_poupanca(), 0.02)
    
    def test_get_taxa_impost(self):
        banco = Banco(taxa_imposto=0.005)
        self.assertEqual(banco.get_taxa_imposto(), 0.005)

    def test_set_taxa_imposto(self):
        banco = Banco()
        banco.set_taxa_imposto(0.01)
        self.assertEqual(banco.get_taxa_imposto(), 0.01)

    def test_cadastrar_imposto(self): # BUG 8
        banco = Banco(taxa_imposto=0.01)
        conta_imposto = ContaImposto('9876')
        banco.cadastrar(conta_imposto)
        self.assertEqual(conta_imposto.get_taxa(), 0.01, "Taxa de imposto não aplicada no cadastro")

    def test_set_taxa_imposto_atualiza_contas(self):  # BUG 9
        banco = Banco(taxa_imposto=0.001)
        conta_imposto = ContaImposto('9876')
        banco.cadastrar(conta_imposto)
        banco.set_taxa_imposto(0.005)
        self.assertEqual(conta_imposto.get_taxa(), 0.005, "Taxa de imposto não atualizada nas contas existentes")

    def test_creditar_inverte_operacao(self): # BUG 10
        banco = Banco()
        conta = Conta('1234')
        banco.cadastrar(conta)
        banco.creditar('1234', 100)
        self.assertEqual(conta.get_saldo(), 100.0, "Operação de crédito invertida")

    def test_debitar_inverte_operacao(self): # BUG 11
        banco = Banco()
        conta = Conta('1234')
        banco.cadastrar(conta)
        banco.creditar('1234', 100)  # Creditar primeiro para poder debitar
        banco.debitar('1234', 50)
        self.assertEqual(conta.get_saldo(), 50.0, "Operação de débito invertida")
    
    def test_get_saldo(self): # BUG 12
        banco = Banco()
        conta = Conta('12345')
        banco.cadastrar(conta)
        banco.creditar('12345', 100.0)
        self.assertEqual(banco.saldo('12345'), 100.0, "Retorno incorreto do saldo")

if __name__ == '__main__':
    unittest.main()