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

Navegue até o diretório `tarefa_de_programacao_01` no terminal e execute os scripts de teste individualmente usando o comando python <nome_do_arquivo.py>, por exemplo:
```
python testa_calculadora.py
python testa_conversores.py
python testa_matematica.py
```
