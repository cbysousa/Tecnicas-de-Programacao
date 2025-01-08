import unittest

from sisbanco import Conta, Banco, ContaAbstrata, ContaEspecial, ContaImposto, ContaPoupanca

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

class TestContaImposto(unittest.TestCase):
    def test_debitar(self):
        pass

    def test_get_taxa(self):
        pass

    def test_set_taxa(self):
        pass

class TestBanco(unittest.TestCase):
    def test_casdastrar(self):
        pass

    def test_procurar(self):
        pass

    def test_creditar(self):
        pass

    def test_debitar(self):
        pass

    def test_saldo(self):
        pass

    def test_transferir(self):
        pass

    def test_get_taxa_poupanca(self):
        pass

    def test_set_taxa_poupanca(self):
        pass

if __name__ == '__main__':
    unittest.main()