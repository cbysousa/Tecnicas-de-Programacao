from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
   def __init__(self, numero:str):
      self.__numero = numero
      self._saldo = 0.0
    
   def creditar(self, valor: float) -> None:
      self._saldo += valor

   @abstractmethod
   def debitar(self, valor:float) -> None:
      pass

   def get_numero(self)-> str:
    return self.__numero

   def get_saldo(self)-> float:
    return self._saldo

class Conta(ContaAbstrata):
  def __init__(self, numero:str): 
    super().__init__(numero)
    
  def debitar(self, valor:float) -> None:
    self._saldo = self._saldo - valor   

class ContaPoupanca(Conta):
   def __init__(self, numero:str):
      super().__init__(numero)

   def render_juros(self, taxa: float) -> None:
    self.creditar(self.get_saldo() * taxa)

class ContaEspecial(Conta):
  def __init__(self, numero: str):
    super().__init__(numero)
    self.__bonus = 0

  def get_bonus(self):
     return self.__bonus
  
  def render_bonus(self) -> None:
     super().creditar(self.__bonus)
     self.__bonus = 0

  def creditar(self, valor:float) -> None: #toda vez que utilizamos o método CREDITAR, incrementamos o atributo BONUS com 1% do valor creditado
     self.__bonus += valor * 0.01
     super().creditar(valor)

class ContaImposto(ContaAbstrata):
   def __init__(self, numero:str):
      super().__init__(numero)
      self.__taxa = 0.01

   def debitar(self, valor:float) -> None:
      self._saldo = self._saldo - (valor + (valor * self.__taxa))
    
   def get_taxa(self) -> None:
      return self.__taxa
   
   def set_taxa(self, taxa: float) -> None:
      self.__taxa = taxa

class Banco:
    def __init__(self, taxaP, taxaI):
      self.__contas = []
      self.__taxaPoupanca:float = taxaP
      self.__taxaImposto:float = taxaI

    def cadastrar(self, conta:ContaAbstrata) -> None:
        self.__contas.append(conta)

    def procurar(self, numero:str) -> ContaAbstrata:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditarB(self, numero:str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
          conta.creditar(valor)
          print(f"Valor R${valor} creditado com sucesso na conta {numero}!")
        else:
           print(" !..:::CONTA INEXISTENTE :::..!")

    def debitarB(self, numero:str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)
            print(f"Valor R${valor} debitado com sucesso na conta {numero}!")
        else:
           print(" !..:::CONTA INEXISTENTE :::..!")

    def saldoB(self, numero:str) -> float:
        conta = self.procurar(numero)
        if conta is not None:
            print(f"Saldo da conta {numero} é de: R${conta.get_saldo()}")
        else:
            print(" !..:::CONTA INEXISTENTE :::..!")
            return None

    def transferir(self, origem:str, destino:str, valor: float) -> None:
        contaOrigem = self.procurar(origem)  #retorna uma CONTA
        contaDestino = self.procurar(destino) #retorna uma conta
        if contaOrigem is not None and contaDestino is not None:
            if valor > contaOrigem.get_saldo():
               print(f"Saldo na conta {origem} é insuficiente!")
            else: 
              contaOrigem.debitar(valor)
              contaDestino.creditar(valor)
              print(f"Transferência no valor de {valor}R$ da conta {origem} para a conta {destino} feita com sucesso!")
        else:
            print(" !..:::CONTA INEXISTENTE :::..!")
            return None
        
    def renderJuros(self, numero:str) -> None:
       conta = self.procurar(numero)
       if conta is not None and isinstance(conta, ContaPoupanca):
          conta.render_juros(self.__taxaCorrecao)
          print(f"Saldo com juros: {conta.get_saldo()}")
       else:
          print("A conta informada não é do tipo POUPANÇA, ou é INEXISTENTE")
          return None
       
    def get_taxa_Poupanca(self) -> float:
       return self.__taxaPoupanca
    
    def set_taxa_Poupanca(self,taxa) -> None:
       self.__taxaPoupanca = taxa

    def renderBonus(self, numero:str) -> None:
       conta = self.procurar(numero)
       if conta is not None and isinstance(conta, ContaEspecial):
          conta.render_bonus()
          print(f"Saldo com bônus: {conta.get_saldo()}")
       else:
          print("A conta informada não é do tipo ESPECIAL, ou é INEXISTENTE")
          return None
       
    def get_taxa_Imposto(self) -> float:
       return self.__taxaImposto
    
    def set_taxa_Imposto(self, taxa:float) -> None:
       self.__taxaImposto = taxa
       for conta in self.__contas:
         if isinstance(conta, ContaImposto) == True:
            conta.set_taxa(taxa)
       print(f"Taxa atualizada com sucesso!\nNova taxa de imposto = {taxa}")