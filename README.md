# Python
Curso de Python do Curso em Vídeo  
Repositório mostrando como fui desenvolvendo Python.

## Aula #04 - Primeiros Comandos em Python 3

A aula #04 do Curso em Vídeo marca o início prático no Python 3, ensinando como interagir com o computador através de scripts reais.

### Conteúdo Prático:
* **`print()`**: Função de saída de dados na tela.
* **`input()`**: Função de entrada de dados pelo teclado.
* **`=`**: Operador de atribuição (lido como "recebe").
* **`+`**: Operador de adição (para números) ou concatenação (para textos).
* **`,`**: Separador de argumentos dentro do `print()`.

## Aula #05 - Instalando o PyCharm e o QPython3

A aula #05 do Curso em Vídeo é uma aula especial voltada à preparação do ambiente de desenvolvimento. Nela, é explicada a importância da prática por meio de exercícios e como configurar ferramentas para programar tanto no computador quanto no celular.

### Ferramentas e Configurações:
* **PyCharm Community**: Instalação e configuração da IDE (Ambiente de Desenvolvimento Integrado) no Windows, Mac OS e Linux, utilizando o tema *Darcula*.
* **QPython3 / KPython3**: Instalação e uso de um interpretador Python 3 diretamente no celular Android, permitindo treinar em qualquer lugar.
* **Criação de Projetos**: Organização de scripts dentro de um único projeto unificado no PyCharm e a importância da extensão `.py` nos arquivos.
* **Interface da IDE**: Como ajustar o tamanho da fonte (`Settings > Editor > Colors & Fonts`), abrir o console interativo e alternar a execução de arquivos utilizando o menu `Run`.

## Aula #06 - Tipos Primitivos e Saída de Dados

A aula #06 do Curso em Vídeo introduz os conceitos de manipulação de tipos primitivos, coerção de dados (*type casting*), formatação moderna de saídas e métodos para validação de strings.

### Conceitos Práticos e Comandos Novidades:
* **`type()`**: Descobre o tipo primitivo atual de um dado ou variável (ex: retorna `<class 'str'>`).
* **`int()`**: Converte o dado para Número Inteiro (ex: `7`, `-4`).
* **`float()`**: Converte o dado para Número Real/Ponto Flutuante (ex: `4.5`).
* **`bool()`**: Converte o dado para Booleano (retorna `True` se houver conteúdo ou `False` se estiver vazio).
* **`str()`**: Converte o dado para String/Texto (ex: `'Olá'`).
* **`.format()`**: Método para formatação de strings utilizando máscaras `{}` para injetar variáveis no texto.

### Métodos de Validação de String (Funções `is...`):
* **`.isnumeric()`**: Verifica se a string contém apenas dígitos numéricos.
* **`.isalpha()`**: Verifica se a string contém apenas letras.
* **`.isalnum()`**: Verifica se a string é alfanumérica (contém letras e/ou números).
* **`.isupper()`**: Verifica se todas as letras da string estão em maiúsculas.
* **`.islower()`**: Verifica se todas as letras da string estão em minúsculas.
* **`.isspace()`**: Verifica se a string é composta apenas por espaços em branco.
* **`.isprintable()`**: Verifica se a string possui apenas caracteres visíveis que podem ser impressos na tela (ignora quebras de linha como `\n`).

## Aula #07 - Operadores Aritméticos

A aula #07 do Curso em Vídeo detalha como realizar operações matemáticas no Python, a importância da ordem de precedência e novos truques visuais para formatar dados na saída de tela.

### Operadores Aritméticos:
* **`+`**: Adição.
* **`-`**: Subtração.
* **`*`**: Multiplicação (também usado para replicação de strings, ex: `'=' * 20`).
* **`/`**: Divisão (sempre gera um resultado do tipo `float`).
* **`**`**: Potência ou Exponenciação (também calculada pela função nativa **`pow(x, y)`**).
* **`//`**: Divisão Inteira (ignora o resto e devolve apenas o quociente inteiro).
* **`%`**: Resto da Divisão (Módulo).

> **💡 Dica da aula:** Para calcular a raiz quadrada de um número, basta elevá-lo a meio `(de onde vem: num ** (1/2))`.

### Ordem de Precedência:
1. `()`
2. `**`
3. `*`, `/`, `//`, `%` (quem aparecer primeiro, da esquerda para a direita)
4. `+`, `-`

### Modificadores de Formatação (Injetados nas máscaras `{}`):
* **`:.2f`**: Limita a exibição de números reais a uma quantidade fixa de casas decimais (neste exemplo, 2 casas decimais).
* **`{:20}`**: Reserva um espaço fixo de 20 caracteres para o dado.
* **`{:>20}`**: Alinha o texto à direita dentro do espaço de 20 caracteres.
* **`{:<20}`**: Alinha o texto à esquerda dentro do espaço de 20 caracteres.
* **`{:^20}`**: Centraliza o texto dentro do espaço de 20 caracteres.
* **`{:=^20}`**: Centraliza o texto e preenche os espaços vazios ao redor com o caractere informado (neste caso, `=`).

### Controle de Fluxo de Impressão:
* **`end=''`**: Parâmetro inserido no fim do `print()` que impede a quebra de linha automática, juntando o resultado ao próximo `print()`.
* **`\n`**: Caractere especial inserido dentro de strings para forçar uma quebra de linha em qualquer ponto do texto.

## Aula #08 - Utilizando Módulos

A aula #08 do Curso em Vídeo ensina como expandir as capacidades nativas do Python através da importação de módulos (bibliotecas). É apresentado o conceito de inclusão de ferramentas tanto da biblioteca padrão (*built-in*) quanto de pacotes externos.

### Comandos de Importação:
* **`import <modulo>`**: Importa todas as funcionalidades de uma biblioteca para o código. Exige o uso do prefixo ao chamar a função (ex: `math.sqrt()`).
* **`from <modulo> import <funcao>`**: Importa apenas uma ou mais ferramentas específicas de uma biblioteca. Otimiza o uso de memória e dispensa o uso do prefixo no código.

### Novas Bibliotecas e Funções Nativas:

#### Módulo `math` (Matemática Avançada)
* **`sqrt()`**: Calcula a raiz quadrada de um número.
* **`ceil()`**: Arredonda um número com ponto flutuante para cima (teto).
* **`floor()`**: Arredonda um número com ponto flutuante para baixo (chão).
* **`trunc()`**: Elimina a parte decimal de um número, mantendo apenas a parte inteira (trunca o valor).
* **`factorial()`**: Calcula o fatorial de um número inteiro.

#### Módulo `random` (Geração Aleatória)
* **`random()`**: Gera um número real (float) aleatório entre 0.0 e 1.0.
* **`randint(x, y)`**: Gera um número inteiro aleatório dentro de um intervalo fechado entre os valores `x` e `y`.

### Conceitos Extras:
* **PyPI (Python Package Index)**: Repositório público e oficial onde a comunidade Python armazena pacotes e bibliotecas de terceiros (exemplificado na aula com a instalação e importação do módulo externo `emoji`).

## Aula #09 - Manipulando Texto

A aula #09 do Curso em Vídeo ensina como realizar operações avançadas com strings (cadeias de caracteres). São abordados conceitos de fatiamento de texto, análise, transformação, divisão e junção de strings.

### Fatiamento de Strings (Slicing `[]`):
* **`frase[x]`**: Seleciona o caractere localizado no índice `x` (lembrando que o índice começa em 0).
* **`frase[x:y]`**: Extrai uma fatia que vai do índice `x` até o índice `y-1`.
* **`frase[x:y:z]`**: Extrai do índice `x` até o índice `y-1`, pulando de `z` em `z` caracteres.
* **`frase[:y]`**: Fatiamento que começa automaticamente do índice `0` e vai até `y-1`.
* **`frase[x:]`**: Fatiamento que começa no índice `x` e vai até o final da string.
* **`frase[x::z]`**: Começa no índice `x`, vai até o final da string, pulando de `z` em `z`.

### Análise de String:
* **`len(frase)`**: Função nativa que retorna o comprimento total (quantidade de caracteres) da string.
* **`.count('x')`**: Conta quantas vezes o caractere ou sub-string `'x'` aparece na string.
* **`.count('x', início, fim)`**: Conta a ocorrência de `'x'` aplicando um fatiamento interno do índice `início` até `fim-1`.
* **`.find('xyz')`**: Procura pela sub-string `'xyz'` e retorna o índice de onde ela se inicia. Caso não exista na string, retorna `-1`.
* **`'xyz' in frase`**: Operador lógico que verifica a existência da sub-string `'xyz'` dentro da string, retornando `True` ou `False`.

### Transformação de String:
* **`.replace('antigo', 'novo')`**: Procura pela sub-string `'antigo'` e substitui todas as ocorrências por `'novo'`.
* **`.upper()`**: Transforma todas as letras da string em maiúsculas.
* **`.lower()`**: Transforma todas as letras da string em minúsculas.
* **`.capitalize()`**: Transforma apenas o primeiro caractere da string inteira em maiúsculo, forçando o restante para minúsculo.
* **`.title()`**: Analisa as quebras de espaços e transforma a primeira letra de cada palavra em maiúscula.
* **`.strip()`**: Remove os espaços em branco inúteis no início e no fim da string.
* **`.rstrip()`**: Remove apenas os espaços em branco inúteis do lado direito (fim) da string.
* **`.lstrip()`**: Remove apenas os espaços em branco inúteis do lado esquerdo (início) da string.

### Divisão e Junção:
* **`.split()`**: Divide a string em uma lista de palavras, utilizando os espaços em branco como separador padrão (gera uma nova indexação para cada palavra isolada).
* **`'separador'.join(lista)`**: Junta os elementos de uma lista de strings em uma única string única, utilizando o `'separador'` definido entre eles (ex: `'-'.join(palavras)`).

### Recurso Extra de Impressão:
* **Aspas Triplas (`"""..."""`)**: Permite realizar a impressão de blocos longos de textos ou textos com múltiplas linhas de forma direta no código, mantendo a formatação e as quebras de linha originais sem a necessidade de usar múltiplos modificadores `\n`.

## Aula #10 - Condições (Parte 1)

A aula #10 do Curso em Vídeo introduz o conceito de estruturas de controle, especificamente as estruturas condicionais simples e compostas. O foco está no desvio de fluxo de execução do código baseado em testes lógicos e na importância vital da indentação no Python.

### Estruturas de Controle e Palavras-Chave:
* **`if <condição>:`**: Estrutura condicional simples. Bloco de código que só será executado se o resultado do teste lógico for verdadeiro (`True`).
* **`else:`**: Complemento para estrutura condicional composta. Define o bloco de código alternativo que será executado caso a condição do `if` seja falsa (`False`).

### Conceitos Estruturais e Novidades:

#### Indentação de Blocos (Alinhamento)
Diferente de outras linguagens que usam chaves `{}`, o Python utiliza estritamente o alinhamento de espaços (geralmente 4 espaços ou 1 Tab) para determinar quais linhas pertencem a qual bloco de execução (bloco `True` ou bloco `False`).
* **Bloco Verdadeiro:** Linhas indentadas logo abaixo do `if`.
* **Bloco Falso:** Linhas indentadas logo abaixo do `else`.
* **Fluxo Sequencial:** Código sem indentação (no início da linha) continua sendo executado normalmente após as condições terminarem.

#### Condição Simplificada (Operador Ternário)
Forma compacta de escrever uma estrutura condicional composta em uma única linha, útil para atribuições rápidas ou exibições diretas.
* **Exemplo de Sintaxe:** `print('Novo' if tempo <= 3 else 'Velho')`

## Aula #11 - Cores no Terminal

A aula #11 do Curso em Vídeo ensina como customizar a saída visual de dados no terminal utilizando o padrão de códigos de escape ANSI. O conteúdo foca em como modificar o estilo da fonte, a cor do texto e a cor de fundo diretamente dentro de strings.

### Padrão ANSI de Cores (`\033[style;text;backm`):
* **`\033[`**: Código de escape inicial necessário para abrir a configuração de estilo.
* **`m`**: Caractere de fechamento que valida a sequência ANSI.
* **`\033[m`**: Código de **reset**. Limpa todas as formatações anteriores e impede que a cor configurada "vaze" para as próximas linhas do terminal.

### Parâmetros de Estilo (Style):
* **`0`**: *None* (Sem estilo/Padrão).
* **`1`**: *Bold* (Texto em negrito).
* **`4`**: *Underline* (Texto sublinhado).
* **`7`**: *Negative* (Inverte as cores escolhidas, transformando a cor do texto em fundo e vice-versa).

### Parâmetros de Cores do Texto (Text):
* **`30`**: Branco / Cinza claro
* **`31`**: Vermelho
* **`32`**: Verde
* **`33`**: Amarelo
* **`34`**: Azul
* **`35`**: Magenta
* **`36`**: Ciano
* **`37`**: Cinza escuro / Branco do sistema

### Parâmetros de Cores de Fundo (Back):
* **`40`** até **`47`**: Seguem exatamente a mesma ordem cromática das cores de texto (30 a 37), mas aplicam o preenchimento ao plano de fundo do caractere.

## Aula #12 - Condições Aninhadas

A aula #12 marca o início do **Mundo 2** e introduz o conceito de estruturas condicionais aninhadas. O foco está em expandir as decisões de caminhos binários (verdadeiro/falso) para cenários com múltiplas possibilidades de escolha, utilizando uma estrutura de "ninho" (uma condição dentro da outra).

### Palavras-Chave e Estruturas Novas:
* **`elif <condição>:`**: Uma contração de *else if* (senão se). Permite criar desvios condicionais intermediários. Ele só é testado se o `if` inicial (ou o `elif` anterior) for falso (`False`). 

### Conceitos Estruturais:
* **Múltiplas Opções:** Diferente do `else`, que não aceita condições e apenas captura o que sobrou, o `elif` exige um novo teste lógico.
* **Regras de Construção:** * Todo bloco condicional começa obrigatoriamente com **um** único `if`.
    * Pode conter **nenhum ou infinitos** `elif`, dependendo de quantas opções você precisa testar.
    * Pode terminar com **nenhum ou no máximo um** `else` (para fechar o bloco e capturar qualquer exceção).

## Exemplo de uso

### Condicionais Aninhadas (`if`, `elif`, `else`)
```python
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    print('Acessando o menu de suporte técnico...')
elif opcao == 2:
    print('Acessando o laboratório de redes...')
else:
    print('Opção inválida!')
```


## Aula #13 - Estrutura de Repetição for

A aula #13 do Curso em Vídeo introduz o conceito de estruturas de repetição (laços ou *loops*), especificamente o laço com variável de controle `for`. O foco é aprender a automatizar a execução de blocos de código que precisam se repetir por um número pré-determinado de vezes.

### Palavras-Chave e Funções Novas:
* **`for <variável> in <sequência>:`**: Declaração do laço de repetição. A `<variável>` de controle assume o valor de cada elemento da `<sequência>` a cada iteração.
* **`range(stop)`**: Função que gera uma sequência numérica iterável. Se passar apenas um argumento, a contagem começa em `0` e vai até `stop - 1`.
* **`range(start, stop)`**: Gera a sequência numérica iniciando no número `start` e terminando exatamente no número `stop - 1`.
* **`range(start, stop, step)`**: Gera a sequência de `start` até `stop - 1`, mas pulando os números de acordo com o intervalo definido em `step` (passo).

### Conceitos Práticos e Lógicos:
* **Contagem Regressiva:** Para fazer o laço contar de trás para frente, basta utilizar um `step` negativo (ex: `range(6, 0, -1)` faz a contagem de 6 até 1).
* **Parâmetros Dinâmicos:** Os argumentos de início, fim e passo da função `range()` podem ser definidos dinamicamente utilizando variáveis coletadas do usuário.
* **Variável Acumuladora (Somatório):** Conceito de criar uma variável antes do laço (geralmente iniciando em `0`) e utilizá-la dentro do escopo do `for` para somar e acumular valores a cada iteração (ex: `soma = soma + n` ou `soma += n`).

# Exemplo de uso

```python
Contagem progressiva pulando de 2 em 2 (Início, Fim-1, Passo)
for c in range(0, 10, 2):
    print(c)  # Exibe na tela: 0, 2, 4, 6, 8
```

## Aula #14 - Estrutura de Repetição while

A aula #14 do Curso em Vídeo introduz o conceito de laços de repetição baseados em testes lógicos através da estrutura `while`. O foco é aprender a criar repetições flexíveis, ideais para cenários onde o número exato de iterações é desconhecido no momento da escrita do código.

### Palavras-Chave e Estruturas Novas:
* **`while <condição>:`**: Declaração do laço de repetição condicional. Executa o bloco de código indentado repetidamente enquanto a `<condição>` testada retornar verdadeira (`True`).

### Conceitos Práticos e Lógicos:
* **Laço com Teste Lógico:** Ao contrário do `for` (que atua sobre um intervalo ou sequência predefinida), o `while` testa uma condição a cada início de iteração para decidir se continua ou interrompe o fluxo.
* **Flag (Ponto de Parada / Sentinela):** Estratégia de utilizar um valor específico inserido pelo usuário ou calculado pelo sistema para sinalizar o fim da repetição (ex: manter o laço rodando até que o usuário digite o número `0`).
* **Loop Infinito:** Situação que ocorre quando a condição lógica do `while` nunca é atualizada para falsa (`False`) dentro do escopo do laço, fazendo com que o programa execute indefinidamente até ser interrompido externamente.

# Exemplo de uso

Executa repetidamente até que o usuário insira a Flag de parada
```python
resposta = ''
while resposta != 'S':
    resposta = str(input('Deseja encerrar o programa? [S/N]: ')).upper().strip()

print('Programa finalizado com sucesso.')
```

## Aula #15 - Interrompendo repetições while

A aula #15 encerra o **Mundo 2** e ensina como interromper loops de forma abrupta utilizando estruturas de repetição infinitas. Além disso, introduz a forma mais moderna e utilizada de formatação de strings no Python atual.

### Palavras-Chave e Comandos Novos:
* **`while True:`**: Cria um laço de repetição infinito que rodará continuamente até encontrar uma instrução de interrupção explícita no código.
* **`break`**: Comando de interrupção imediata. Quando executado, ele "quebra" o laço de repetição atual (seja `while` ou `for`) e joga o fluxo do programa para a primeira linha logo após o bloco do laço.
* **`f-strings` (Interpolação de Strings)**: Recurso moderno (Python 3.6+) que substitui o método `.format()`. Permite colocar as variáveis diretamente dentro da string adicionando o prefixo `f` antes das aspas.

### Exemplo de uso:
```python
soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break  # O número 999 não entra na soma, o laço para aqui
    soma += num

# Uso da f-string com máscara de formatação de casas decimais integrada
print(f'A soma total dos valores digitados foi {soma}.')
print(f'Exemplo de formatação monetária: R${soma:.2f}')
```

## Aula #16 - Tuplas (Variáveis Compostas)

A aula #16 inicia o **Mundo 3** e introduz o conceito de Variáveis Compostas, começando pelas **Tuplas**. O foco é aprender a gerenciar coleções de dados que permitem armazenar múltiplos valores em uma única variável, respeitando a estrutura de indexação.

### Características Fundamentais:
* **Imutabilidade:** Regra de ouro da aula — *"As tuplas são imutáveis"*. Uma vez que a tupla é criada, o programa não pode alterar, adicionar ou remover nenhum elemento dela até que a execução termine.
* **Sintaxe e Flexibilidade:** Identificada historicamente pelo uso de parênteses `()`. Aceitam dados de tipos primitivos misturados dentro da mesma estrutura.

### Novos Comandos e Métodos:
* **`enumerate()`**: Retorna simultaneamente o índice (posição) e o valor de cada elemento da tupla a cada iteração do laço.
* **`sorted()`**: Organiza os elementos para exibição (ordem alfabética ou numérica), gerando uma nova estrutura sem alterar a tupla original.
* **`.index('x')`**: Busca o elemento `'x'` e retorna a sua primeira posição de índice encontrada.
* **`.index('x', pos)`**: Realiza a busca pelo elemento `'x'`, mas inicia o rastreio a partir da posição `pos` informada (útil para ignorar ocorrências anteriores).
* **`del()`**: Apaga uma variável inteira diretamente da memória do sistema.

### Comportamento de Operadores Existentes:
* **Adição de Tuplas (`+`)**: Realiza uma **concatenação** (junção), unindo os elementos de duas ou mais tuplas em uma nova estrutura, respeitando a ordem declarada.

### Exemplos Práticos de Sintaxe:

```python
# 1. Criando uma tupla e a regra de imutabilidade
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# lanche[1] = 'Refrigerante'  # ❌ Se desentalar, gera erro: 'tuple' object does not support item assignment

# 2. Utilizando sorted() e enumerate()
# sorted() exibe em ordem alfabética: ('Hambúrguer', 'Pizza', 'Pudim', 'Suco')
for posicao, comida in enumerate(sorted(lanche)):
    print(f'Vou comer {comida} na posição {posicao}')

# 3. Operador + e o método .index()
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # Gera uma nova tupla: (2, 5, 4, 5, 8, 1, 2)

print(c.index(5))     # Retorna 1 (índice da primeira ocorrência do número 5)
print(c.index(5, 2))  # Retorna 3 (busca o número 5 começando a partir da posição 2)

# 4. Deletando da memória
del(lanche)
# print(lanche)  # ❌ Gera erro NameError porque a variável deixou de existir
```

## Aula #17 - Listas (Parte 1)

A aula #17 introduz a segunda estrutura de variável composta: as **Listas**. Diferente das tuplas, as listas são a ferramenta ideal para armazenar coleções de dados dinâmicas, pois são totalmente mutáveis e expansíveis.

### Características Fundamentais:
* **Mutabilidade:** Regra de ouro da aula — *"As listas são mutáveis"*. É possível alterar, adicionar ou remover qualquer elemento da estrutura a qualquer momento da execução.
* **Sintaxe:** Identificada pelo uso de colchetes `[]` ou através da função construtora `list()`.

### Novos Comandos e Métodos:
* **`.append(item)`**: Adiciona dinamicamente um novo elemento ao final da lista (aumentando o tamanho da estrutura automaticamente).
* **`.insert(pos, item)`**: Inserts um novo elemento em uma posição de índice específica (`pos`), deslocando todos os elementos seguintes para a direita.
* **`del lista[índice]`**: Remove um elemento da lista baseado na sua posição de índice.
* **`.pop(índice)`**: Remove um elemento baseado no índice. Se chamado sem argumentos (`.pop()`), remove automaticamente o último elemento da lista.
* **`.remove(valor)`**: Remove um elemento baseado no seu conteúdo/valor real (elimina apenas a primeira ocorrência encontrada da esquerda para a direita).
* **`.sort()`**: Organiza todos os elementos da lista em ordem crescente (alfabética ou numérica) diretamente na estrutura original (*in-place*).
* **`.sort(reverse=True)`**: Organiza todos os elementos da lista diretamente em ordem decrescente.

### Peculiaridades do Python (Ligação vs Cópia):
* **Ligação (`b = a`)**: No Python, se você igualar uma lista à outra, o sistema cria uma **ligação** (referência) entre elas. Qualquer alteração feita na lista `b` modificará automaticamente a lista `a`.
* **Cópia (`b = a[:]`)**: Para duplicar os dados de uma lista criando uma estrutura totalmente independente na memória, utiliza-se o fatiamento completo `[:]`.

### Exemplos Práticos de Sintaxe:

```python
# 1. Criando e modificando elementos (Mutabilidade)
num = [2, 5, 9, 1]
num[2] = 3  # Substitui o valor do índice 2 (muda de 9 para 3)

# 2. Inserindo novos elementos
num.append(7)         # Lista vira: [2, 5, 3, 1, 7]
num.insert(1, 0)      # Insere o 0 na posição 1. Lista vira: [2, 0, 5, 3, 1, 7]

# 3. Removendo elementos com segurança
num.pop()             # Remove o último (7). Lista vira: [2, 0, 5, 3, 1]
num.pop(1)            # Remove o elemento da posição 1 (0). Lista vira: [2, 5, 3, 1]

if 5 in num:
    num.remove(5)     # Remove o valor 5. Lista vira: [2, 3, 1]

# 4. Ordenação de dados
num.sort()            # Organiza em ordem crescente: [1, 2, 3]
num.sort(reverse=True) # Organiza em ordem decrescente: [3, 2, 1]

# 5. Comportamento de Cópia vs Ligação
lista_original = [8, 2, 5]

# Forma errada (Cria ligação):
lista_link = lista_original
lista_link[0] = 9     # Altera AMBAS as listas!

# Forma correta (Cria cópia independente):
lista_copia = lista_original[:]
lista_copia[0] = 4    # Altera apenas a 'lista_copia'

## Aula #18 - Listas (Parte 2)

A aula #18 aprofunda o estudo das listas, introduzindo o conceito de **Listas Aninhadas** (listas dentro de listas). A estrutura evolui de uma coleção linear simples para uma organização multidimensional, permitindo modelar matrizes e tabelas complexas de dados.

### Características Fundamentais:
* **Estruturas Aninhadas:** Elementos de uma lista principal podem ser, por si só, outras listas completas.
* **Indexação Bidimensional (Dupla):** Para acessar um dado específico dentro de uma lista aninhada, utilizam-se dois pares de colchetes: o primeiro indica a posição da sub-lista na lista principal, e o segundo indica o índice do elemento dentro daquela sub-lista.

### Novos Comandos e Métodos:
* **`.clear()`**: Limpa completamente todos os elementos de uma lista, deixando-a vazia (`[]`), sem apagar a variável da memória.
* **Cópia de Escopo Interno (`.append(lista[:])`)**: Ao trabalhar com estruturas aninhadas alimentadas por uma lista temporária, o uso do fatiamento completo `[:]` é **obrigatório** antes de aplicar o `.clear()`. Caso contrário, a lista principal receberá apenas referências vazias.

### Exemplos Práticos de Sintaxe:

```python
# 1. Declaração direta e Indexação Dupla
povo = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(povo[0])       # Exibe a sub-lista inteira: ['Pedro', 25]
print(povo[1][0])    # Acessa o índice 0 da sub-lista 1: 'Maria'
print(povo[2][1])    # Acessa o índice 1 da sub-lista 2: 32

# 2. Estrutura de repetição em Listas Compostas
for pessoa in povo:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

# 3. Alimentando listas compostas dinamicamente (O perigo do .clear())
galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    
    # ❌ galera.append(dado) -> ERRADO: criaria uma ligação. Ao limpar 'dado', 'galera' esvazia.
    galera.append(dado[:]) #  CORRETO: joga uma cópia dos valores atuais para a lista principal
    dado.clear()           # Limpa a estrutura temporária para a próxima iteração

print(galera)
