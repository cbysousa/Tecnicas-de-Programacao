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

class TestContaPoupanca(unittest.TestCase):
    def test_render_juros(self):
        conta = ContaPoupanca('54321')
        conta.creditar(50)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 55)

class TestContaEspecial(unittest.TestCase):
    def test_render_bonus(self):
        conta = ContaEspecial('1234')
        conta.creditar(valor=100)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101.0)

    def test_creditar_especial(self): #incompleto
        conta = ContaEspecial('40028922')
        conta.creditar(200)
        self.assertEqual(conta.get_saldo(), 200)
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

if __name__ == '__main__':
    unittest.main()