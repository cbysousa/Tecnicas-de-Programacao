class Conta:
    def __init__(self, numero:str):
       self.__numero = numero
       self.__saldo = 0

    def creditar(self, valor:float) -> None:
       self.__saldo += valor

    def debitar(self, valor:float) -> None:
       self.__saldo -= valor

    def get_numero(self) -> str:
       return self.__numero

    def get_saldo(self) -> float:
       return self.__saldo
    
class ContaPoupanca:
    def __init__(self, numero:str):
        super().__init__(numero)
        
    def render_juros(self, taxa:float) -> None:
        self.creditar(self.get_saldo() * taxa)

class ContaEspecial:
    def __init__(self, numero:str):
        super().__init__(numero)
        self.__bonus = 0
    
    def render_bonus(self, taxa:float) -> None:
        super().creditar(self.__bonus)
        self.__bonus = 0

    def creditar(self, valor:float) -> None:
       self.__saldo += valor * 0.1
       super().creditar(valor)

class Banco:
    def __init__(self, taxa:float):
        self.__contas = []

    def cadastrar(self, conta:Conta) -> None:
        self.__contas.append(conta)
   
    def procurar(self, numero:str) -> Conta:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None
   
    def creditar(self, numero:str, valor:float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)
    def debitar(self, numero:str, valor:float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)
        else:
            print("Conta não existente!")

    def saldo(self, numero:str) -> float:
        conta = self.procurar(numero)
        if conta is not None:
            print(f"O saldo atual da conta é de R${conta.get_saldo()}")
        else: print("Conta não existente!")

    def transferir(self, origem:str, destino:str, valor:float) -> None:
        conta_origem = self.procurar(origem)
        conta_destino = self.procurar(destino)
        if conta_origem is not None and conta_destino is not None:
            saldo_origem = conta_origem.get_saldo()
            if saldo_origem >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print("Transferência realizada com sucesso!")
            else: print("A conta de Origem não possui saldo suficiente!")
        else: print("Uma das contas não existe!")

    def render_juros(self, numero:str):
        conta = self.procurar(numero)
        if conta is not None and isinstance(conta, ContaPoupanca):
            conta.render_juros(self.__taxa)
        else:
            print('A conta não existe ou não é uma conta poupança!')

    def get_taxa(self) -> float:
        return self.__taxa

    def set_taxa(self, taxa:float) -> None:
        self.__taxa = taxa

    def reder_bonus(self, numero:str) -> None:
        conta = self.procurar(numero)
        if conta is not None and isinstance(conta, ContaEspecial):
            conta.render_bonus()
        else: 
            print('A conta não existe ou não é uma conta especial!')
