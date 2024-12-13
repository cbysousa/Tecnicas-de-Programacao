# Técnicas de Programação

## Primeira tarefa (TP01):
A primeira tarefa é focada na criação e organização de módulos e pacotes em Python, abordando conceitos como importação, escopo de variáveis, testes e estrutura de projetos.

- Módulo `calculadora.py`: Implementa as operações matemáticas básicas (soma, subtração, multiplicação e divisão) com dois operandos. O arquivo `testa_calculadora.py` contém testes unitários para cada operação, usando valores fixos e importando o módulo `calculadora` com o alias `calc`.

- Memória na `calculadora.py`: Adicionada a funcionalidade de "memória" ao módulo `calculadora`. Uma variável global `acumulador` armazena o resultado da última operação. As funções foram modificadas para usar o `acumulador` como primeiro operando caso apenas um argumento seja fornecido. `testa_calculadora.py` foi atualizado com testes para essa nova funcionalidade.

- Módulo `conversores.py`: Implementa funções de conversão de unidades (Celsius-Fahrenheit, metros-pés, quilômetros-milhas, dias-horas). O arquivo `testa_conversores.py` realiza testes para cada função de conversão, importando o módulo conversores.

- Pacote `matematica]`: Criado o pacote `matematica` com os módulos `aritmetica.py` (soma e subtração) e `geometria.py` (área do círculo e retângulo). O arquivo `testa_matematica.py` importa o pacote e testa as funções de ambos os módulos.

- `__init__.py` no Pacote matematica: Adicionado o arquivo `__init__.py` ao pacote `matematic`a para importar automaticamente as funções dos módulos `aritmetica` e `geometria`, simplificando a importação no arquivo principal `testa_matematica.py`.

- Subpacote `estatistica`: Criado o subpacote `matematica/estatistica` contendo o módulo `media.py` com a função `media_simples`. O arquivo `testa_matematica.py` foi atualizado para importar e testar a função `media_simples` usando a sintaxe `from matematica.estatistica import media`.

### Como Executar os Testes:

Navegue até o diretório `tarefa_de_programacao_01` no terminal e execute os scripts de teste individualmente usando uma das opções abaixo:
1. Especificando o caminho completo:
```
python tarefa_de_programacao_01/testa_calculadora.py
python tarefa_de_programacao_01/testa_conversores.py
python tarefa_de_programacao_01/testa_matematica.py
```
2. Navegando até o diretório e executando:
```
cd tarefa_de_programacao_01
python testa_calculadora.py
python testa_conversores.py
python testa_matematica.py
```

## Segunda tarefa (TP02):
A segunda tarefa possui foco na Programação Orientada a Objetos em Python, abordando conceitos como criação de classes, métodos, encapsulamento e interação com objetos. A tarefa foi dividida em cinco etapas principais:

Criando um Módulo Calculadora Orientado a Objetos: Implementar uma classe `Calculadora` com métodos para as quatro operações matemáticas básicas (soma, subtração, multiplicação e divisão). Criar testes unitários para validar a funcionalidade da classe.

Adicionando Memória à Calculadora: Estender a classe `Calculadora` para incluir um atributo privado `acumulador` que armazena o resultado da última operação. Modificar os métodos para utilizar o `acumulador` quando apenas um operando for fornecido. Atualizar os testes unitários para contemplar a nova funcionalidade.

Implementando a classe Conta: Criar uma classe `Conta` com métodos para creditar, debitar, obter número da conta e obter saldo.

Implementando a classe Banco: Implementar uma classe Banco com métodos para cadastrar contas, procurar contas, creditar em contas, debitar de contas, consultar saldo e realizar transferências entre contas.

Interagindo com o Sistema Bancário: Desenvolver um programa que simula um terminal de atendimento bancário, utilizando as classes `Conta` e `Banco`. O programa permite que o usuário crie contas e realize operações de crédito, débito, transferência e consulta de saldo.

Os arquivos relevantes para esta tarefa estão localizados no diretório tarefa_de_programacao_02. Instruções mais detalhadas sobre cada etapa, incluindo a especificação das classes e métodos, podem ser encontradas no enunciado da TP02 (https://github.com/cbysousa/Tecnicas-de-Programacao/blob/main/tarefa_de_programacao_02/TP02.pdf).

# Terceira Tarefa (TP03):
A terceira tarefa expande o projeto do Sistema Bancário (SisBanco) desenvolvido na TP02, utilizando conceitos avançados de Programação Orientada a Objetos, como herança, sobrescrita de métodos e polimorfismo. As funcionalidades implementadas nesta etapa são:

#### Classe `ContaPoupanca`:
- Foi criada uma classe derivada de `Conta` chamada `ContaPoupanca`.
- Adicionada a funcionalidade de render juros com base em uma taxa fornecida.
A classe possibilita calcular os rendimentos para contas de poupança ao final de um período.

#### Classe `ContaEspecial`:

- Foi criada outra classe derivada de `Conta` chamada `ContaEspecial`.
- O método `creditar` foi sobrescrito para incluir um *bônus incremental* em cada crédito.
- Adicionada a funcionalidade de render bônus acumulados.

#### Rendimentos no Banco:

A classe `Banco` foi estendida para suportar:
- Render juros em contas poupança com base em uma taxa privada de correção do banco.
- Render bônus em contas especiais.
Também foram incluídos métodos para configurar e consultar a taxa de juros do banco.

#### Interface do Sistema Bancário:

O módulo `terminal_atendimento.py` foi atualizado para incluir as seguintes opções no menu principal:
- [5] Render Juros: Calcula os rendimentos de uma conta poupança.
- [6] Render Bônus: Converte bônus acumulados em saldo para contas especiais.
- [7] Alterar Taxa de Juros: Permite ao banco configurar uma nova taxa de correção para poupança.

## Como Executar o Sistema:
Acesse o diretório da TP03 no terminal e execute o arquivo `terminal_atendimento.py`.
Use as opções do menu para testar as novas funcionalidades, como rendimentos e gerenciamento de contas.
