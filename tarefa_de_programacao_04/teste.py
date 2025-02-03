from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
   def __init__(self, numero:str):
      self.__numero = numero
      self.__saldo = 0.0

   def creditar(self, valor:float) -> None:
      self.__saldo += valor

   @abstractmethod
   def debitar(self, valor:float) -> None:
      pass

   def get_numero(self) -> str:
      return self.__numero

   def get_saldo(self) -> float:
      return self.__saldo
   

class Conta(ContaAbstrata):
   def __init__(self, numero:str):
      super().__init__(numero)

   def debitar(self, valor:float) -> None:
      self.__saldo += valor

conta = Conta("123")

conta.creditar(1000)
conta.debitar(200)



'''from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
   def __init__(self, numero:str):
      self.__numero = numero
      self.__saldo = 0.0
    
   def creditar(self, valor: float) -> None:
      self.__saldo += valor

   @abstractmethod
   def debitar(self, valor:float) -> None:
      pass

   def get_numero(self)-> str:
    return self.__numero

   def get_saldo(self)-> float:
    return self.__saldo

class Conta(ContaAbstrata):
  def __init__(self, numero:str): 
    super().__init__(numero)

  def debitar(self, valor:float) -> None:
    self.__saldo -= valor   


def teste():
  conta = Conta("123")
  print(conta.creditar(1000))
  print(conta.get_saldo())
  print(conta.debitar(100))
  print(conta.get_saldo())

print(teste())'''

'''class Pai:
    def __init__(self, sobrenome, time):
        self.__sobrenome = sobrenome
        self.__time  = time
        self.__carteira = 0


class Filho(Pai):
    def __init__(self, sobrenome, time):
        super().__init__(sobrenome, time)
   
    def printar_sobrenome(self):
        self.__sobrenome = self.__sobrenome.upper()
        return self.__sobrenome


p = Pai("Ferreira", "Vasco")
f = Filho("Ferreira", "Vasco")
print(f.printar_sobrenome())'''