# -*- coding: utf-8 -*-
"""
Script gerador da Lista 11 e seus gabaritos individuais.
"""
import os

BASE_DIR = "/Users/jodafons/Desktop/codes/rap-2026/latex/Listas/body/Lista_11"
ANSWERS_DIR = os.path.join(BASE_DIR, "answers")
os.makedirs(ANSWERS_DIR, exist_ok=True)

questions_data = []

# ==============================================================================
# TEMA 1: Fundamentos, Variáveis, Operadores e Funções Básicas (Q1 a Q10)
# ==============================================================================

questions_data.append({
    "num": 1,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Considere a seguinte expressão aritmética executada em Python para calcular o valor total de uma compra com desconto:
\begin{minted}{python}
total = 10 + 2 * 3 ** 2 - 8 // 4 + 7 % 3
\end{minted}
Qual será o valor final atribuído à variável \code{total}?

\begin{itemize}[leftmargin=*]
    \item \textbf{Dica:} A ordem de precedência dos operadores aritméticos em Python é: 1º Parênteses \code{()}, 2º Exponenciação \code{**}, 3º Multiplicação \code{*}, Divisão \code{/}, Divisão Inteira \code{//} e Módulo \code{\%} (avaliados da esquerda para a direita), 4º Adição \code{+} e Subtração \code{-} (avaliados da esquerda para a direita). O operador de divisão inteira \code{//} retorna apenas a parte inteira da divisão (ex: \code{8 // 4} resulta em \code{2}), enquanto o operador módulo \code{\%} calcula o resto da divisão inteira (ex: \code{7 % 3} resulta em \code{1}).
\end{itemize}

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item 25
    \item 27
    \item 28
    \item 30
    \item 19
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
A ordem de precedência dos operadores em Python é:
1. Exponenciação: $3 ** 2 = 9$
2. Multiplicação, divisão inteira e módulo (da esquerda para a direita):
   $2 * 9 = 18$, $8 // 4 = 2$, $7 \% 3 = 1$
3. Adição e subtração:
   $10 + 18 - 2 + 1 = 28 - 2 + 1 = 27$.
}"""
})

questions_data.append({
    "num": 2,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Em Python, a conversão explícita de tipos (\emph{type casting}) é muito utilizada ao processar dados de formulários web. Analise as quatro conversões abaixo:
\begin{minted}{python}
v1 = int(7.89)
v2 = float("42.5")
v3 = bool("")
v4 = bool(0)
\end{minted}
Quais são, respectivamente, os valores e tipos resultantes armazenados em \code{v1}, \code{v2}, \code{v3} e \code{v4}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{7} (int), \code{42.5} (float), \code{False} (bool), \code{False} (bool)
    \item \code{8} (int), \code{42.5} (float), \code{True} (bool), \code{False} (bool)
    \item \code{7} (int), \code{42.5} (float), \code{True} (bool), \code{True} (bool)
    \item \code{7.89} (float), \code{42.5} (float), \code{False} (bool), \code{False} (bool)
    \item \code{8} (int), \code{42} (int), \code{False} (bool), \code{False} (bool)
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (A)}

\textbf{Justificativa:}
* \code{int(7.89)} trunca a parte decimal, resultando no inteiro \code{7}.
* \code{float("42.5")} converte a string no float \code{42.5}.
* \code{bool("")} converte string vazia para o booleano \code{False}.
* \code{bool(0)} converte o número zero para o booleano \code{False}.
}"""
})

questions_data.append({
    "num": 3,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Sobre a diferença fundamental entre a instrução \code{print()} e o comando \code{return} dentro de uma função em Python, assinale a alternativa \textbf{CORRETA}:

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{print()} armazena o valor em uma variável externa, enquanto \code{return} apenas exibe no terminal.
    \item \code{print()} apenas exibe uma representação visual no console (efeito colateral), enquanto \code{return} devolve o dado para quem chamou a função e encerra sua execução.
    \item Toda função que possui \code{print()} necessariamente retorna um valor numérico diferente de \code{None}.
    \item O comando \code{return} é opcional e, caso omitido, a função sempre retornará a última mensagem impressa pelo \code{print()}.
    \item \code{return} só pode ser utilizado para retornar números inteiros, enquanto \code{print()} funciona para qualquer tipo.
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
\code{print()} é uma função de saída padrão que exibe dados na tela (efeito colateral). Já o \code{return} envia o resultado da computação de volta para o ponto de chamada do programa e finaliza imediatamente a execução da função. Sem \code{return}, a função devolve implicitamente \code{None}.
}"""
})

questions_data.append({
    "num": 4,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Um viajante está planejando uma viagem internacional e precisa converter a previsão do tempo de graus Celsius para Fahrenheit. A fórmula de conversão é:
\[
F = C \times 1.8 + 32
\]
Escreva uma função chamada \code{celsius_para_fahrenheit} que receba a temperatura em Celsius e retorne o valor equivalente em Fahrenheit.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def celsius_para_fahrenheit(celsius: float) -> float:}
    \item \textbf{Entrada:} \code{25.0}
    \item \textbf{Saída:} \code{77.0}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def celsius_para_fahrenheit(
    celsius: float,
) -> float:
    return celsius * 1.8 + 32.0
\end{minted}
}"""
})

questions_data.append({
    "num": 5,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Um supermercado está aplicando descontos percentuais no caixa. Escreva uma função chamada \code{aplicar_desconto} que receba o preço original de um produto (em reais) e a porcentagem de desconto (de 0 a 100) e retorne o valor final a ser pago pelo consumidor.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def aplicar_desconto(preco_original: float, porcentagem_desconto: float) -> float:}
    \item \textbf{Entrada:} \code{150.0, 10.0}
    \item \textbf{Saída:} \code{135.0}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def aplicar_desconto(
    preco_original: float,
    porcentagem_desconto: float,
) -> float:
    desconto = (
        preco_original
        * (porcentagem_desconto / 100.0)
    )
    return preco_original - desconto
\end{minted}
}"""
})

questions_data.append({
    "num": 6,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Em uma clínica de nutrição, o Índice de Massa Corporal (IMC) é calculado pela fórmula:
\[
\text{IMC} = \frac{\text{peso}}{\text{altura}^2}
\]
onde o peso é dado em quilogramas e a altura em metros. Escreva uma função chamada \code{calcular_imc} que receba o peso e a altura de um paciente e retorne o valor do seu IMC.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def calcular_imc(peso_kg: float, altura_m: float) -> float:}
    \item \textbf{Entrada:} \code{70.0, 1.75}
    \item \textbf{Saída:} \code{22.857142857142858}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def calcular_imc(
    peso_kg: float,
    altura_m: float
) -> float:
    return peso_kg / (altura_m ** 2)
\end{minted}
}"""
})

questions_data.append({
    "num": 7,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Um grupo de amigos foi a uma pizzaria e deseja dividir a conta em partes iguais. Ao valor consumido, deve ser acrescida a taxa de serviço de $10\%$. Escreva uma função chamada \code{rachar_conta} que receba o valor total consumido (em reais) e o número de pessoas na mesa, retornando o valor individual a ser pago por cada amigo.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def rachar_conta(valor_total: float, num_pessoas: int) -> float:}
    \item \textbf{Entrada:} \code{200.0, 4}
    \item \textbf{Saída:} \code{55.0}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def rachar_conta(
    valor_total: float,
    num_pessoas: int
) -> float:
    total_com_taxa = valor_total * 1.10
    return total_com_taxa / num_pessoas
\end{minted}
}"""
})

questions_data.append({
    "num": 8,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Em uma disciplina de programação, a média final de um estudante é calculada por uma média ponderada de três avaliações, com pesos 2, 3 e 5, respectivamente:
\[
\text{Média} = \frac{N_1 \times 2 + N_2 \times 3 + N_3 \times 5}{2 + 3 + 5}
\]
Escreva uma função chamada \code{media_ponderada_provas} que receba as três notas em ponto flutuante e retorne a média final ponderada calculada.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def media_ponderada_provas(n1: float, n2: float, n3: float) -> float:}
    \item \textbf{Entrada:} \code{6.0, 7.0, 8.0}
    \item \textbf{Saída:} \code{7.3}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def media_ponderada_provas(
    n1: float,
    n2: float,
    n3: float,
) -> float:
    soma = (
        n1 * 2.0 + n2 * 3.0 + n3 * 5.0
    )
    return soma / 10.0
\end{minted}
}"""
})

questions_data.append({
    "num": 9,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Um caixa eletrônico de autoatendimento precisa dispensar o menor número de cédulas possível para um determinado valor de saque inteiro (múltiplo de 10). O caixa dispõe de cédulas de R\$ 50, R\$ 20 e R\$ 10. Sem utilizar laços ou condicionais, escreva uma função chamada \code{sacar_cedulas} que receba o valor total do saque e retorne uma tupla com a quantidade de cédulas de 50, 20 e 10, nesta ordem.

\begin{itemize}[leftmargin=*]
    \item \textbf{Dica:} O operador de divisão inteira \code{//} obtém a quantidade inteira de vezes que um número cabe no outro (ex.: \code{180 // 50} resulta em \code{3}), enquanto o operador módulo \code{\%} obtém o resto da divisão (ex.: \code{180 % 50} resulta em \code{30}).
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def sacar_cedulas(}\\\code{    valor_reais: int}\\\code{) -> Tuple[int, int, int]:}
    \item \textbf{Entrada:} \code{180}
    \item \textbf{Saída:} \code{(3, 1, 1)}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def sacar_cedulas(
    valor_reais: int,
) -> Tuple[int, int, int]:
    c50 = valor_reais // 50
    resto50 = valor_reais % 50
    
    c20 = resto50 // 20
    resto20 = resto50 % 20
    
    c10 = resto20 // 10
    return c50, c20, c10
\end{minted}
}"""
})

questions_data.append({
    "num": 10,
    "tema": "Tema 1: Fundamentos, Variáveis, Operadores e Funções Básicas",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""Um investidor deseja calcular o montante acumulado em uma aplicação de renda fixa sob o regime de juros compostos. A fórmula matemática do montante é:
\[
M = P \times (1 + i)^t
\]
onde $P$ é o capital inicial investido, $i$ é a taxa de juros mensal expressa em decimal (ex: 1\% = 0.01) e $t$ é o número de meses de aplicação. Escreva uma função chamada \code{calcular_montante_juros_compostos} que receba o capital inicial, a taxa de juros mensal e o prazo em meses, e retorne o montante final acumulado.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def calcular_montante_juros_compostos(}\\\code{    capital_inicial: float,}\\\code{    taxa_mensal: float, meses: int}\\\code{) -> float:}
    \item \textbf{Entrada:} \code{1000.0, 0.01, 12}
    \item \textbf{Saída:} \code{1126.8250301319697}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def calcular_montante_juros_compostos(
    capital_inicial: float,
    taxa_mensal: float,
    meses: int
) -> float:
    fator = (1.0 + taxa_mensal) ** meses
    return capital_inicial * fator
\end{minted}
}"""
})

# ==============================================================================
# TEMA 2: Estruturas Condicionais e Lógica Booleana (Q11 a Q25)
# ==============================================================================

questions_data.append({
    "num": 11,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Em Python, a avaliação de expressões lógicas com os operadores \code{and} e \code{or} segue a regra do curto-circuito (\emph{short-circuit evaluation}). Considere as variáveis:
\begin{minted}{python}
a = False
b = True
c = True
\end{minted}
Qual é o resultado da expressão lógica: \code{a and (b or c) or (not a and b)}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{False}
    \item \code{True}
    \item \code{None}
    \item Erro de sintaxe por excesso de parênteses
    \item \code{1}
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
1. \code{a and (b or c)} avalia \code{a} (que é \code{False}), portanto essa primeira parte resulta em \code{False} por curto-circuito.
2. \code{not a} resulta em \code{True}. \code{not a and b} é \code{True and True}, que resulta em \code{True}.
3. \code{False or True} resulta em \code{True}.
}"""
})


questions_data.append({
    "num": 13,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Considere o seguinte trecho de código em Python:
\begin{minted}{python}
x = [1, 2, 3]
y = [1, 2, 3]
resultado1 = (x == y)
resultado2 = (x is y)
\end{minted}
Quais são os valores booleanos de \code{resultado1} e \code{resultado2}?

\begin{itemize}[leftmargin=*]
    \item \textbf{Dica:} O operador \code{==} compara a \textbf{igualdade de valor/conteúdo} entre os objetos, enquanto o operador \code{is} compara a \textbf{identidade}, verificando se as variáveis apontam para a mesma referência/endereço na memória (\code{id(x) == id(y)}).
\end{itemize}

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{True} e \code{True}
    \item \code{False} e \code{False}
    \item \code{True} e \code{False}
    \item \code{False} e \code{True}
    \item \code{None} e \code{False}
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (C)}

\textbf{Justificativa:}
\begin{itemize}
    \item O operador \code{==} compara a \textbf{igualdade de valores/conteúdo} dos objetos, retornando \code{True} pois as duas listas possuem os mesmos elementos.
    \item O operador \code{is} compara a \textbf{identidade de memória} (\code{id(x) == id(y)}). Como \code{x} e \code{y} são listas distintas alocadas em posições de memória diferentes, o resultado é \code{False}.
\end{itemize}
}"""
})

questions_data.append({
    "num": 14,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Analise o seguinte bloco condicional em Python:
\begin{minted}{python}
pontos = 75
if pontos >= 90:
    categoria = "Ouro"
elif pontos >= 70:
    categoria = "Prata"
elif pontos >= 50:
    categoria = "Bronze"
else:
    categoria = "Iniciante"
\end{minted}
Qual valor estará armazenado na variável \code{categoria} ao final da execução?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{"Ouro"}
    \item \code{"Prata"}
    \item \code{"Bronze"}
    \item \code{"Iniciante"}
    \item \code{"Prata"} e em seguida \code{"Bronze"}
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
No bloco \code{if/elif/else}, a execução ocorre de cima para baixo e para no **primeiro** ramo cuja condição for verdadeira. Como \code{pontos = 75}, a primeira condição (\code{pontos >= 90}) é falsa, mas a segunda (\code{pontos >= 70}) é verdadeira. O valor \code{"Prata"} é atribuído e o restante da estrutura é ignorado.
}"""
})

questions_data.append({
    "num": 15,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Uma instituição de ensino adota o seguinte critério de avaliação acadêmica baseado na média final do discente:
\begin{itemize}
    \item Média $\ge 7.0$: \code{"APROVADO"}
    \item $5.0 \le \text{Média} < 7.0$: \code{"RECUPERACAO"}
    \item Média $< 5.0$: \code{"REPROVADO"}
\end{itemize}
Escreva uma função chamada \code{status_aluno} que receba a média do aluno e retorne a string com seu status correspondente.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def status_aluno(nota_media: float) -> str:}
    \item \textbf{Entrada:} \code{6.4} | \textbf{Saída:} \code{"RECUPERACAO"}
    \item \textbf{Entrada:} \code{8.5} | \textbf{Saída:} \code{"APROVADO"}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def status_aluno(nota_media: float) -> str:
    if nota_media >= 7.0:
        return "APROVADO"
    elif nota_media >= 5.0:
        return "RECUPERACAO"
    else:
        return "REPROVADO"
\end{minted}
}"""
})

questions_data.append({
    "num": 16,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Para se cadastrar como motorista em uma plataforma de transporte, a pessoa precisa ter no mínimo 18 anos de idade e possuir Carteira Nacional de Habilitação (CNH) válida. Escreva uma função chamada \code{pode_dirigir} que receba a idade (inteiro) e um booleano indicando se possui CNH, retornando \code{True} se a pessoa estiver apta a dirigir ou \code{False} caso contrário.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def pode_dirigir(idade: int, possui_cnh: bool) -> bool:}
    \item \textbf{Entrada:} \code{19, True} | \textbf{Saída:} \code{True}
    \item \textbf{Entrada:} \code{17, True} | \textbf{Saída:} \code{False}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def pode_dirigir(
    idade: int,
    possui_cnh: bool,
) -> bool:
    return (
        idade >= 18 and possui_cnh
    )
\end{minted}
}"""
})

questions_data.append({
    "num": 17,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{classificar_inteiro} que receba um número inteiro e o classifique em uma das quatro categorias: \code{"PAR_POSITIVO"}, \code{"PAR_NEGATIVO"}, \code{"IMPAR_POSITIVO"} ou \code{"IMPAR_NEGATIVO"}. Caso o número seja zero, a função deve retornar \code{"ZERO"}.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def classificar_inteiro(numero: int) -> str:}
    \item \textbf{Entrada:} \code{-4} | \textbf{Saída:} \code{"PAR_NEGATIVO"}
    \item \textbf{Entrada:} \code{7} | \textbf{Saída:} \code{"IMPAR_POSITIVO"}
    \item \textbf{Entrada:} \code{0} | \textbf{Saída:} \code{"ZERO"}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def classificar_inteiro(
    numero: int,
) -> str:
    if numero == 0:
        return "ZERO"
    
    paridade = (
        "PAR" if numero % 2 == 0
        else "IMPAR"
    )
    sinal = (
        "POSITIVO" if numero > 0
        else "NEGATIVO"
    )
    return f"{paridade}_{sinal}" 
\end{minted}
}"""
})

questions_data.append({
    "num": 18,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""No calendário gregoriano comercial, um ano é considerado bissexto se for divisível por 4, exceto se for divisível por 100, a menos que também seja divisível por 400. Escreva uma função chamada \code{eh_ano_bissexto} que receba o ano (número inteiro) e retorne \code{True} se for bissexto ou \code{False} caso contrário.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def eh_ano_bissexto(ano: int) -> bool:}
    \item \textbf{Entrada:} \code{2024} | \textbf{Saída:} \code{True}
    \item \textbf{Entrada:} \code{1900} | \textbf{Saída:} \code{False}
    \item \textbf{Entrada:} \code{2000} | \textbf{Saída:} \code{True}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def eh_ano_bissexto(ano: int) -> bool:
    div_4_nao_100 = (
        ano % 4 == 0
        and ano % 100 != 0
    )
    div_400 = (ano % 400 == 0)
    return div_4_nao_100 or div_400
\end{minted}
}"""
})

questions_data.append({
    "num": 19,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Um e-commerce adota a seguinte política de entrega: o frete é totalmente gratuito (\code{0.0}) se o valor da compra for estritamente superior a R\$ 200,00 ou se o cliente for membro do programa VIP. Em qualquer outro caso, o valor do frete é fixo em R\$ 25,00. Escreva uma função chamada \code{calcular_frete} que implemente essa regra de negócio.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def calcular_frete(valor_compra: float, cliente_vip: bool) -> float:}
    \item \textbf{Entrada:} \code{150.0, True} | \textbf{Saída:} \code{0.0}
    \item \textbf{Entrada:} \code{180.0, False} | \textbf{Saída:} \code{25.0}
    \item \textbf{Entrada:} \code{250.0, False} | \textbf{Saída:} \code{0.0}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def calcular_frete(
    valor_compra: float,
    cliente_vip: bool
) -> float:
    if valor_compra > 200.0 or cliente_vip:
        return 0.0
    return 25.0
\end{minted}
}"""
})

questions_data.append({
    "num": 20,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Para que três segmentos de reta $a, b, c$ formem um triângulo válido, cada lado deve ser estritamente menor que a soma dos outros dois ($a < b + c$, $b < a + c$, $c < a + b$). Caso formem um triângulo, ele pode ser: \code{"EQUILATERO"} (3 lados iguais), \code{"ISOSCELES"} (2 lados iguais) ou \code{"ESCALENO"} (3 lados diferentes). Se não formarem triângulo, retorne \code{"INVALIDO"}. Escreva uma função chamada \code{tipo_triangulo}.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def tipo_triangulo(a: float, b: float, c: float) -> str:}
    \item \textbf{Entrada:} \code{5.0, 5.0, 8.0} | \textbf{Saída:} \code{"ISOSCELES"}
    \item \textbf{Entrada:} \code{1.0, 2.0, 10.0} | \textbf{Saída:} \code{"INVALIDO"}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def tipo_triangulo(
    a: float,
    b: float,
    c: float,
) -> str:
    if not (
        a < b + c
        and b < a + c
        and c < a + b
    ):
        return "INVALIDO"
    
    if a == b == c:
        return "EQUILATERO"
    elif (
        a == b or a == c or b == c
    ):
        return "ISOSCELES"
    else:
        return "ESCALENO" 
\end{minted}
}"""
})

questions_data.append({
    "num": 21,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Considere uma tabela progressiva de Imposto de Renda mensal simplificada:
\begin{itemize}
    \item Até R\$ 2.000,00: Isento (\code{0.0})
    \item De R\$ 2.000,01 a R\$ 4.000,00: Alíquota de 10\% sobre a parcela que exceder R\$ 2.000,00
    \item Acima de R\$ 4.000,00: R\$ 200,00 fixos mais 20\% sobre a parcela que exceder R\$ 4.000,00
\end{itemize}
Escreva uma função chamada \code{calcular_ir_simplificado} que receba o salário bruto e retorne o valor do imposto devido.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def calcular_ir_simplificado(salario_bruto: float) -> float:}
    \item \textbf{Entrada:} \code{3500.0} | \textbf{Saída:} \code{150.0}
    \item \textbf{Entrada:} \code{5000.0} | \textbf{Saída:} \code{400.0}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def calcular_ir_simplificado(
    salario_bruto: float
) -> float:
    if salario_bruto <= 2000.0:
        return 0.0
    elif salario_bruto <= 4000.0:
        excesso = salario_bruto - 2000.0
        return excesso * 0.10
    else:
        excesso = salario_bruto - 4000.0
        return 200.0 + (excesso * 0.20)
\end{minted}
}"""
})

questions_data.append({
    "num": 22,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Um aplicativo de caronas cobra uma tarifa base de R\$ 5,00 mais R\$ 2,50 por quilômetro rodado. Caso a corrida ocorra em horário de pico, aplica-se um acréscimo de 30\% sobre o valor total da corrida. Se estiver chovendo, é somada uma taxa adicional fixa de segurança de R\$ 4,00. Escreva uma função chamada \code{calcular_corrida} que receba a distância em km, se é horário de pico e se está chovendo, retornando o preço final.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def calcular_corrida(}\\\code{    distancia_km: float,}\\\code{    horario_pico: bool, esta_chovendo: bool}\\\code{) -> float:}
    \item \textbf{Entrada:} \code{10.0, True, True} | \textbf{Saída:} \code{43.0}
    \item \textbf{Entrada:} \code{10.0, False, False} | \textbf{Saída:} \code{30.0}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def calcular_corrida(
    distancia_km: float,
    horario_pico: bool,
    esta_chovendo: bool
) -> float:
    valor_base = 5.0 + (distancia_km * 2.50)
    if horario_pico:
        valor_base *= 1.30
    if esta_chovendo:
        valor_base += 4.0
    return valor_base
\end{minted}
}"""
})

questions_data.append({
    "num": 23,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{validar_cadastro_usuario} que valide os dados de cadastro de um novo cliente em um sistema bancário digital. Os critérios obrigatórios são:
1. Idade deve ser maior ou igual a 18 e menor ou igual a 120 anos.
2. O email não pode ser vazio e deve conter o caractere \code{"@"} e pelo menos um caractere \code{"."}.
3. A renda mensal declarada não pode ser negativa.
A função deve retornar uma tupla contendo um booleano (\code{True} se todos os critérios forem atendidos, \code{False} caso contrário) e uma mensagem explicativa (\code{"CADASTRO_VALIDO"} ou a causa da reprovação: \code{"ERRO_IDADE"}, \code{"ERRO_EMAIL"} ou \code{"ERRO_RENDA"}).

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def validar_cadastro_usuario(}\\\code{    idade: int, email: str, renda: float}\\\code{) -> Tuple[bool, str]:}
    \item \textbf{Entrada:} \code{25, "joao@email.com", 3000.0} | \textbf{Saída:} \code{(True, "CADASTRO_VALIDO")}
    \item \textbf{Entrada:} \code{16, "ana@email.com", 1500.0} | \textbf{Saída:} \code{(False, "ERRO_IDADE")}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def validar_cadastro_usuario(
    idade: int,
    email: str,
    renda: float,
) -> Tuple[bool, str]:
    if not (18 <= idade <= 120):
        return False, "ERRO_IDADE"
    if (
        "@" not in email
        or "." not in email
    ):
        return False, "ERRO_EMAIL"
    if renda < 0:
        return False, "ERRO_RENDA"
    return True, "CADASTRO_VALIDO" 
\end{minted}
}"""
})

questions_data.append({
    "num": 24,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""Uma plataforma de streaming deseja recomendar o plano ideal para um usuário com base em suas preferências técnicas:
\begin{itemize}
    \item \textbf{Plano Básico:} Suporta no máximo 1 tela simultânea, resolução padrão HD e não permite download offline.
    \item \textbf{Plano Padrão:} Suporta até 2 telas simultâneas, resolução Full HD (não 4K) e permite download offline.
    \item \textbf{Plano Premium:} Suporta até 4 telas simultâneas, resolução 4K Ultra HD e permite download offline.
\end{itemize}
Escreva uma função chamada \code{recomendar_plano_streaming} que receba o número de telas desejadas, se o usuário exige 4K e se exige download offline. A função deve retornar o nome do plano mais econômico que atenda plenamente aos requisitos (\code{"PLANO_BASICO"}, \code{"PLANO_PADRAO"}, \code{"PLANO_PREMIUM"}) ou \code{"PLANO_CUSTOMIZADO"} se exceder 4 telas.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def recomendar_plano_streaming(}\\\code{    num_telas: int, requer_4k: bool,}\\\code{    requer_download: bool}\\\code{) -> str:}
    \item \textbf{Entrada:} \code{2, False, True} | \textbf{Saída:} \code{"PLANO_PADRAO"}
    \item \textbf{Entrada:} \code{1, True, False} | \textbf{Saída:} \code{"PLANO_PREMIUM"}
    \item \textbf{Entrada:} \code{5, True, True} | \textbf{Saída:} \code{"PLANO_CUSTOMIZADO"}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def recomendar_plano_streaming(
    num_telas: int,
    requer_4k: bool,
    requer_download: bool,
) -> str:
    if num_telas > 4:
        return "PLANO_CUSTOMIZADO"
    
    if (
        requer_4k
        or num_telas > 2
    ):
        return "PLANO_PREMIUM"
    
    if (
        requer_download
        or num_telas > 1
    ):
        return "PLANO_PADRAO"
    
    return "PLANO_BASICO" 
\end{minted}
}"""
})

questions_data.append({
    "num": 25,
    "tema": "Tema 2: Estruturas Condicionais e Lógica Booleana",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""Um banco analisa pedidos de empréstimo pessoal com base em quatro variáveis: renda mensal líquida, valor da parcela pretendida, pontuação de score de crédito (0 a 1000) e existência de negativação no cadastro de inadimplentes.
As regras de aprovação são:
1. O cliente não pode possuir negativação ativa (\code{tem_divida_ativa == False}).
2. O valor da parcela pretendida não pode ultrapassar $30\%$ da renda mensal líquida.
3. Se o score for $\ge 700$, o empréstimo é aprovado com juros normais (\code{"APROVADO_JUROS_BAIXOS"}).
4. Se o score estiver entre 500 e 699, o empréstimo é aprovado com taxa de risco (\code{"APROVADO_JUROS_ALTOS"}).
5. Se o score for $< 500$, o empréstimo é recusado por risco de crédito (\code{"RECUSADO_SCORE"}).
6. Caso a parcela comprometa mais de 30\% da renda, retorne \code{"RECUSADO_MARGEM"}. Caso haja dívida ativa, retorne \code{"RECUSADO_INADIMPLENCIA"}. A prioridade de rejeição é dívida ativa primeiro, depois margem e depois score.
Escreva a função \code{analisar_credito_bancario}.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def analisar_credito_bancario(}\\\code{    renda_mensal: float, parcela: float,}\\\code{    score: int, tem_divida_ativa: bool}\\\code{) -> Tuple[bool, str]:}
    \item \textbf{Entrada:} \code{5000.0, 1200.0, 750, False} | \textbf{Saída:} \code{(True, "APROVADO_JUROS_BAIXOS")}
    \item \textbf{Entrada:} \code{4000.0, 1500.0, 800, False} | \textbf{Saída:} \code{(False, "RECUSADO_MARGEM")}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def analisar_credito_bancario(
    renda_mensal: float,
    parcela: float,
    score: int,
    tem_divida_ativa: bool,
) -> Tuple[bool, str]:
    if tem_divida_ativa:
        return (
            False,
            "RECUSADO_INADIMPLENCIA",
        )
    if parcela > (
        renda_mensal * 0.30
    ):
        return (
            False,
            "RECUSADO_MARGEM",
        )
    if score < 500:
        return (
            False,
            "RECUSADO_SCORE",
        )
    elif score >= 700:
        return (
            True,
            "APROVADO_JUROS_BAIXOS",
        )
    else:
        return (
            True,
            "APROVADO_JUROS_ALTOS",
        )
\end{minted}
}"""
})

# ==============================================================================
# TEMA 3: Estruturas de Repetição (for e while) (Q26 a Q40)
# ==============================================================================

questions_data.append({
    "num": 26,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Ao executar a instrução \code{list(range(10, 2, -3))} em Python, qual sequência de números inteiros será gerada?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{[10, 7, 4]}
    \item \code{[10, 7, 4, 1]}
    \item \code{[10, 8, 6, 4, 2]}
    \item \code{[10, 7, 4, 2]}
    \item \code{[]} (lista vazia)
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (A)}

\textbf{Justificativa:}
O comando \code{range(start=10, stop=2, step=-3)} inicia em 10 e subtrai 3 a cada iteração enquanto for estritamente maior que o limite de parada (2):
\begin{enumerate}
    \item Primeiro termo: $10$
    \item Segundo termo: $10 - 3 = 7$
    \item Terceiro termo: $7 - 3 = 4$
\end{enumerate}
O próximo seria $4 - 3 = 1$, que já não é $> 2$. Logo, os valores gerados são \code{[10, 7, 4]}.
}"""
})

questions_data.append({
    "num": 27,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Considere o seguinte trecho de código em Python:
\begin{minted}{python}
soma = 0
for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    soma += i
\end{minted}
Qual será o valor final da variável \code{soma}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item 3
    \item 7
    \item 10
    \item 15
    \item 6
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
Rastreando a iteração:
\begin{itemize}
    \item $i = 1$: \code{soma = 0 + 1 = 1}
    \item $i = 2$: \code{soma = 1 + 2 = 3}
    \item $i = 3$: condição \code{i == 3} é verdadeira; o \code{continue} salta para a próxima iteração sem somar.
    \item $i = 4$: \code{soma = 3 + 4 = 7}
    \item $i = 5$: condição \code{i == 5} é verdadeira; o \code{break} interrompe e encerra o laço imediatamente.
\end{itemize}
Valor final de \code{soma} = 7.
}"""
})

questions_data.append({
    "num": 28,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Qual das seguintes situações causa obrigatoriamente um laço infinito (\emph{infinite loop}) em Python?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item Um laço \code{for i in range(1000):} sem o comando \code{break}.
    \item Um laço \code{while condicao:} em que a variável presente na \code{condicao} nunca é modificada no corpo do laço e a condição permanece verdadeira.
    \item Um laço que utiliza \code{continue} na primeira linha do corpo do \code{for}.
    \item Percorrer uma tupla vazia com \code{for item in ():}.
    \item Executar uma chamada recursiva que atinge seu caso base logo na primeira chamada.
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
Em um laço \code{while}, se a condição de controle for inicialmente verdadeira e nenhum comando dentro do bloco modificar as variáveis que a definem (ou executar um \code{break}), a condição nunca se tornará falsa, resultando em um laço infinito.
}"""
})

questions_data.append({
    "num": 29,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Quantas vezes a instrução \code{contador += 1} será executada no trecho abaixo?
\begin{minted}{python}
contador = 0
for i in range(4):
    for j in range(3):
        contador += 1
\end{minted}

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item 7 vezes
    \item 12 vezes
    \item 9 vezes
    \item 16 vezes
    \item 6 vezes
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
O laço externo executa 4 iterações ($i \in \{0, 1, 2, 3\}$). Para cada uma dessas 4 iterações, o laço interno executa 3 iterações ($j \in \{0, 1, 2\}$). O número total de execuções da linha interna é $4 \times 3 = 12$ vezes.
}"""
})

questions_data.append({
    "num": 30,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{somar_pares_intervalo} que receba dois números inteiros positivos (\code{inicio} e \code{fim}, com $\text{inicio} \le \text{fim}$) e, utilizando um laço de repetição \code{for}, calcule e retorne o somatório de todos os números pares pertencentes a esse intervalo fechado.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def somar_pares_intervalo(inicio: int, fim: int) -> int:}
    \item \textbf{Entrada:} \code{1, 10} | \textbf{Saída:} \code{30} *(2 + 4 + 6 + 8 + 10)*
    \item \textbf{Entrada:} \code{4, 4} | \textbf{Saída:} \code{4}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def somar_pares_intervalo(
    inicio: int,
    fim: int
) -> int:
    soma = 0
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            soma += num
    return soma
\end{minted}
}"""
})


questions_data.append({
    "num": 32,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Uma pessoa deseja comprar um equipamento eletrônico e decidiu guardar uma quantia fixa todo mês em um cofrinho (sem juros). Escreva uma função chamada \code{meses_para_meta_financeira} que receba o valor total da meta (em reais) e o valor do aporte mensal constante, utilizando um laço \code{while} para calcular e retornar a quantidade exata de meses necessários para acumular ou ultrapassar a meta.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def meses_para_meta_financeira(meta_reais: float, aporte_mensal: float) -> int:}
    \item \textbf{Entrada:} \code{5000.0, 400.0} | \textbf{Saída:} \code{13}
    \item \textbf{Entrada:} \code{1200.0, 300.0} | \textbf{Saída:} \code{4}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def meses_para_meta_financeira(
    meta_reais: float,
    aporte_mensal: float,
) -> int:
    acumulado = 0.0
    meses = 0
    while acumulado < meta_reais:
        acumulado += aporte_mensal
        meses += 1
    return meses
\end{minted}
}"""
})

questions_data.append({
    "num": 33,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{gerar_tabuada} que receba um número inteiro $N$ e, utilizando um laço \code{for}, retorne uma tupla com os 10 resultados da tabuada de multiplicação de $N$ (de $N \times 1$ até $N \times 10$).

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def gerar_tabuada(numero: int) -> Tuple[int, ...]:}
    \item \textbf{Entrada:} \code{7} | \textbf{Saída:} \code{(7, 14, 21, 28, 35, 42, 49, 56, 63, 70)}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def gerar_tabuada(
    numero: int,
) -> Tuple[int, ...]:
    resultados = []
    for i in range(1, 11):
        resultados.append(numero * i)
    return tuple(resultados)
\end{minted}
}"""
})

questions_data.append({
    "num": 34,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{contar_digitos_codigo} que receba uma string representando um código de rastreio de encomenda (por exemplo, \code{"BR-2024-XP99-88"}) e, iterando caractere por caractere com um laço \code{for}, conte e retorne a quantidade de caracteres numéricos (dígitos de 0 a 9) presentes na string.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def contar_digitos_codigo(codigo: str) -> int:}
    \item \textbf{Entrada:} \code{"PED-2024-X99"} | \textbf{Saída:} \code{6}
    \item \textbf{Entrada:} \code{"SEM_NUMEROS"} | \textbf{Saída:} \code{0}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def contar_digitos_codigo(codigo: str) -> int:
    qtd_digitos = 0
    for char in codigo:
        if "0" <= char <= "9":
            qtd_digitos += 1
    return qtd_digitos
\end{minted}
}"""
})

questions_data.append({
    "num": 35,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""O fatorial de um número natural $n$ (representado por $n!$) é o produto de todos os inteiros positivos menores ou iguais a $n$, com $0! = 1$. Escreva uma função chamada \code{calcular_fatorial} que receba um inteiro não negativo $n$ e calcule seu fatorial utilizando um laço \code{while}.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def calcular_fatorial(n: int) -> int:}
    \item \textbf{Entrada:} \code{5} | \textbf{Saída:} \code{120}
    \item \textbf{Entrada:} \code{0} | \textbf{Saída:} \code{1}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def calcular_fatorial(n: int) -> int:
    resultado = 1
    contador = n
    while contador > 1:
        resultado *= contador
        contador -= 1
    return resultado
\end{minted}
}"""
})

questions_data.append({
    "num": 36,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Um consumidor possui uma dívida de cartão de crédito que rende juros mensais fixos sobre o saldo restante. Todo mês, os juros são aplicados ao saldo devedor ($saldo = saldo \times (1 + taxa)$) e, logo após, o cliente realiza um pagamento fixo. Escreva uma função chamada \code{simular_pagamento_divida} que receba o saldo devedor inicial, a taxa de juros mensal em decimal e o valor do pagamento mensal fixo. A função deve retornar quantos meses serão necessários para quitar totalmente a dívida (saldo $\le 0$). Caso o pagamento mensal seja menor ou igual aos juros do primeiro mês, a dívida nunca será paga; nesse caso, a função deve retornar \code{-1}.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def simular_pagamento_divida(}\\\code{    saldo_devedor: float,}\\\code{    taxa_juros_mensal: float,}\\\code{    pagamento_mensal: float}\\\code{) -> int:}
    \item \textbf{Entrada:} \code{1000.0, 0.02, 200.0} | \textbf{Saída:} \code{6}
    \item \textbf{Entrada:} \code{1000.0, 0.05, 50.0} | \textbf{Saída:} \code{-1}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def simular_pagamento_divida(
    saldo_devedor: float,
    taxa_juros_mensal: float,
    pagamento_mensal: float,
) -> int:
    juros_min = (
        saldo_devedor
        * taxa_juros_mensal
    )
    if pagamento_mensal <= juros_min:
        return -1
    
    meses = 0
    saldo = saldo_devedor
    while saldo > 0:
        juros = (
            saldo * taxa_juros_mensal
        )
        saldo = (
            saldo
            + juros
            - pagamento_mensal
        )
        meses += 1
    return meses
\end{minted}
}"""
})

questions_data.append({
    "num": 37,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Um número inteiro maior que 1 é primo se for divisível apenas por 1 e por ele mesmo. Escreva uma função chamada \code{eh_numero_primo} que receba um número inteiro e utilize um laço \code{for} para verificar se ele é primo, retornando \code{True} ou \code{False}. Números menores ou iguais a 1 não são primos.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def eh_numero_primo(numero: int) -> bool:}
    \item \textbf{Entrada:} \code{17} | \textbf{Saída:} \code{True}
    \item \textbf{Entrada:} \code{21} | \textbf{Saída:} \code{False}
    \item \textbf{Entrada:} \code{1} | \textbf{Saída:} \code{False}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def eh_numero_primo(
    numero: int,
) -> bool:
    if numero <= 1:
        return False
    lim = int(numero ** 0.5) + 1
    for d in range(2, lim):
        if numero % d == 0:
            return False
    return True
\end{minted}
}"""
})

questions_data.append({
    "num": 38,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{extremos_gastos} que receba uma tupla não vazia de valores numéricos representando as despesas do mês e, utilizando apenas estruturas de repetição (sem usar as funções embutidas \code{min()} e \code{max()}), encontre e retorne uma tupla contendo o menor e o maior gasto, exatamente nesta ordem: \code{(menor, maior)}.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def extremos_gastos(gastos: Tuple[float, ...]) -> Tuple[float, float]:}
    \item \textbf{Entrada:} \code{(120.5, 45.0, 890.0, 15.0, 320.0)} | \textbf{Saída:} \code{(15.0, 890.0)}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def extremos_gastos(
    gastos: Tuple[float, ...],
) -> Tuple[float, float]:
    menor = gastos[0]
    maior = gastos[0]
    for v in gastos:
        if v < menor:
            menor = v
        if v > maior:
            maior = v
    return menor, maior
\end{minted}
}"""
})

questions_data.append({
    "num": 39,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""A sequência de Fibonacci é definida por: $F_0 = 0$, $F_1 = 1$ e $F_n = F_{n-1} + F_{n-2}$ para $n \ge 2$. Escreva uma função chamada \code{gerar_fibonacci} que receba a quantidade de termos desejada $N$ ($N \ge 1$) e, utilizando um laço de repetição, gere e retorne uma tupla contendo os $N$ primeiros termos da sequência de Fibonacci.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def gerar_fibonacci(n_termos: int) -> Tuple[int, ...]:}
    \item \textbf{Entrada:} \code{8} | \textbf{Saída:} \code{(0, 1, 1, 2, 3, 5, 8, 13)}
    \item \textbf{Entrada:} \code{2} | \textbf{Saída:} \code{(0, 1)}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def gerar_fibonacci(
    n_termos: int,
) -> Tuple[int, ...]:
    if n_termos <= 0:
        return ()
    if n_termos == 1:
        return (0,)
    
    seq = [0, 1]
    while len(seq) < n_termos:
        prox = seq[-1] + seq[-2]
        seq.append(prox)
    return tuple(seq)
\end{minted}
}"""
})

questions_data.append({
    "num": 40,
    "tema": "Tema 3: Estruturas de Repetição (for e while)",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""Em um jogo de adivinhação numérica, o computador escolhe um número inteiro entre $1$ e um limite superior $N$. Um jogador inteligente utiliza a estratégia da Busca Binária para adivinhar o número no menor número de tentativas possível (sempre chutando o ponto médio do intervalo atual). Escreva uma função chamada \code{passos_busca_binaria} que receba o número secreto (\code{alvo}) e o \code{limite_superior}, e utilize um laço \code{while} para simular essa busca binária, retornando a quantidade de chutes/passos até acertar o número.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def passos_busca_binaria(alvo: int, limite_superior: int) -> int:}
    \item \textbf{Entrada:} \code{73, 100} | \textbf{Saída:} \code{6}
    \item \textbf{Entrada:} \code{50, 100} | \textbf{Saída:} \code{1}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def passos_busca_binaria(
    alvo: int,
    limite_superior: int,
) -> int:
    inicio = 1
    fim = limite_superior
    passos = 0
    while inicio <= fim:
        passos += 1
        meio = (inicio + fim) // 2
        if meio == alvo:
            return passos
        elif meio < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return passos
\end{minted}
}"""
})

# ==============================================================================
# TEMA 4: Strings, Fatiamento e Tuplas (Q41 a Q50)
# ==============================================================================

questions_data.append({
    "num": 41,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Dada a string \code{s = "PROGRAMACAO"}, qual será o resultado da operação de fatiamento \code{s[1:8:2]}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{"RMAA"}
    \item \code{"RGAA"}
    \item \code{"RGA"}
    \item \code{"PGMC"}
    \item \code{"ROAM"}
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
Os índices da string \code{"PROGRAMACAO"} (tamanho 11) são:
\begin{itemize}
    \item Índice 0: 'P'
    \item Índice 1: 'R'
    \item Índice 2: 'O'
    \item Índice 3: 'G'
    \item Índice 4: 'R'
    \item Índice 5: 'A'
    \item Índice 6: 'M'
    \item Índice 7: 'A'
    \item Índice 8: 'C'
\end{itemize}

O fatiamento \code{s[1:8:2]} seleciona os elementos dos índices a partir de 1 até antes de 8 (1, 3, 5 e 7) com passo 2:
\begin{itemize}
    \item \code{s[1]} = 'R'
    \item \code{s[3]} = 'G'
    \item \code{s[5]} = 'A'
    \item \code{s[7]} = 'A'
\end{itemize}
Portanto, o resultado da operação é \code{"RGAA"}.
}"""
})

questions_data.append({
    "num": 42,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Sobre a imutabilidade de strings e tuplas em Python, assinale a afirmação \textbf{CORRETA}:

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item Podemos alterar um elemento de uma tupla diretamente com \code{t[0] = novo_valor} desde que o valor seja do mesmo tipo.
    \item O método \code{texto.replace("a", "b")} modifica a string \code{texto} no mesmo endereço de memória.
    \item Tanto strings quanto tuplas são objetos imutáveis; qualquer operação de concatenação ou substituição gera um novo objeto na memória.
    \item Tuplas que contêm apenas números inteiros são mutáveis, mas tuplas com strings são imutáveis.
    \item É possível deletar um caractere de uma string usando a instrução \code{del texto[0]}.
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (C)}

\textbf{Justificativa:}
Em Python, \code{str} e \code{tuple} são tipos imutáveis. Uma vez alocados na memória, seus elementos internos não podem ser alterados, adicionados ou removidos. Funções e métodos como \code{.replace()}, \code{.upper()} ou operadores de concatenação (\code{+}) constroem e retornam novos objetos.
}"""
})

questions_data.append({
    "num": 43,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Considere a string \code{frase = "  banana,maca,uva  "}. Ao executar o comando:
\begin{minted}{python}
itens = frase.strip().split(",")
\end{minted}
Qual será o valor armazenado na variável \code{itens}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{"banana,maca,uva"}
    \item \code{("banana", "maca", "uva")}
    \item \code{["banana", "maca", "uva"]}
    \item \code{["  banana", "maca", "uva  "]}
    \item \code{"banana maca uva"}
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (C)}

\textbf{Justificativa:}
* \code{frase.strip()} remove os espaços em branco do início e do final da string, resultando em \code{"banana,maca,uva"}.
* \code{.split(",")} divide a string pelo caractere separador vírgula, retornando uma lista de strings: \code{["banana", "maca", "uva"]}.
}"""
})

questions_data.append({
    "num": 44,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Uma palavra ou frase é chamada de palíndromo se for lida da mesma maneira da esquerda para a direita e da direita para a esquerda, desconsiderando espaços em branco e diferenças entre maiúsculas e minúsculas. Escreva uma função chamada \code{eh_palindromo} que receba uma string e retorne \code{True} se for palíndromo ou \code{False} caso contrário.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def eh_palindromo(texto: str) -> bool:}
    \item \textbf{Entrada:} \code{"Apos a sopa"} | \textbf{Saída:} \code{True}
    \item \textbf{Entrada:} \code{"Python"} | \textbf{Saída:} \code{False}
    \item \textbf{Entrada:} \code{"Socorram me subi no onibus em Marrocos"} | \textbf{Saída:} \code{True}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def eh_palindromo(texto: str) -> bool:
    limpo = texto.replace(" ", "").lower()
    return limpo == limpo[::-1]
\end{minted}
}"""
})

questions_data.append({
    "num": 45,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Em trabalhos acadêmicos, a citação de autores no texto segue frequentemente o formato: \code{"SOBRENOME, P."} onde \code{SOBRENOME} é o último sobrenome em maiúsculas e \code{P.} é a primeira letra do primeiro nome seguida de ponto. Escreva uma função chamada \code{formatar_citacao_bibliografica} que receba o nome completo de um autor e retorne a citação formatada.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def formatar_citacao_bibliografica(nome_completo: str) -> str:}
    \item \textbf{Entrada:} \code{"Carlos Eduardo Souza"} | \textbf{Saída:} \code{"SOUZA, C."}
    \item \textbf{Entrada:} \code{"Alan Turing"} | \textbf{Saída:} \code{"TURING, A."}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def formatar_citacao_bibliografica(
    nome_completo: str,
) -> str:
    partes = (
        nome_completo.strip().split()
    )
    prim = partes[0]
    ult = partes[-1]
    return (
        f"{ult.upper()}, "
        f"{prim[0].upper()}."
    )
\end{minted}
}"""
})

questions_data.append({
    "num": 46,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{extrair_dominio_email} que receba uma string contendo um endereço de e-mail válido (ex: \code{"cliente.vip@lojaonline.com.br"}) e utilize os métodos de string para extrair e retornar apenas o domínio (a parte após o símbolo \code{"@"}).

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def extrair_dominio_email(email: str) -> str:}
    \item \textbf{Entrada:} \code{"contato@empresa.com.br"} | \textbf{Saída:} \code{"empresa.com.br"}
    \item \textbf{Entrada:} \code{"usuario@gmail.com"} | \textbf{Saída:} \code{"gmail.com"}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def extrair_dominio_email(email: str) -> str:
    partes = email.strip().split("@")
    return partes[1]
\end{minted}
}"""
})

questions_data.append({
    "num": 47,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Uma loja armazena as informações básicas de cada produto em uma tupla com quatro posições: \code{(codigo: int, nome: str, preco: float, categoria: str)}. Escreva uma função chamada \code{formatar_etiqueta_produto} que receba essa tupla, desempacote seus valores e retorne uma string formatada no padrão: \code{"[CATEGORIA] NOME - R$ PRECO (Cod: CODIGO)"}, onde o preço deve ser exibido com duas casas decimais.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def formatar_etiqueta_produto(produto: Tuple[int, str, float, str]) -> str:}
    \item \textbf{Entrada:} \code{(102, "Teclado Mecanico", 250.0, "Perifericos")}
    \item \textbf{Saída:} \code{"[Perifericos] Teclado Mecanico - R$ 250.00 (Cod: 102)"}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def formatar_etiqueta_produto(
    produto: Tuple[int, str, float, str],
) -> str:
    cod, nome, preco, cat = produto
    return (
        f"[{cat}] {nome} - "
        f"R$ {preco:.2f} (Cod: {cod})"
    )
\end{minted}
}"""
})

questions_data.append({
    "num": 48,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Um servidor web registra cada requisição em uma linha de log formatada por pares chave=valor separados por ponto e vírgula:
\code{"IP=192.168.1.1; STATUS=200; BYTES=4096; PATH=/home"}
Escreva uma função chamada \code{parse_log_web} que receba essa string e faça a extração dos valores, retornando uma tupla tipada contendo \code{(ip: str, status: int, bytes: int, path: str)}.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Tuple}\\\code{def parse_log_web(linha_log: str) -> Tuple[str, int, int, str]:}
    \item \textbf{Entrada:} \\\code{"IP=192.168.1.1; STATUS=200; BYTES=4096; PATH=/home"}
    \item \textbf{Saída:} \\\code{("192.168.1.1", 200, 4096, "/home")}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Tuple

def parse_log_web(
    linha_log: str
) -> Tuple[str, int, int, str]:
    campos = linha_log.strip().split(";")
    ip = campos[0].split("=")[1]
    status = int(campos[1].split("=")[1])
    nbytes = int(campos[2].split("=")[1])
    path = campos[3].split("=")[1]
    return (ip, status, nbytes, path)
\end{minted}
}"""
})

questions_data.append({
    "num": 49,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""A Cifra de César é uma técnica clássica de criptografia por substituição na qual cada letra de uma mensagem em maiúsculas é deslocada um número fixo de posições no alfabeto (considerando o alfabeto de 'A' a 'Z' de 26 letras de forma circular). Caracteres que não sejam letras maiúsculas (como espaços) devem ser mantidos inalterados. Escreva uma função chamada \code{cifrar_texto} que receba a mensagem e o deslocamento inteiro, retornando o texto cifrado.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def cifrar_texto(mensagem: str, deslocamento: int) -> str:}
    \item \textbf{Entrada:} \code{"COMPUTADOR", 3} | \textbf{Saída:} \code{"FRPSXWDGRU"}
    \item \textbf{Entrada:} \code{"ZEBRA", 1} | \textbf{Saída:} \code{"AFCSB"}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def cifrar_texto(
    mensagem: str,
    deslocamento: int,
) -> str:
    res = []
    for ch in mensagem:
        if "A" <= ch <= "Z":
            base = ord("A")
            diff = ord(ch) - base
            offset = (
                diff + deslocamento
            ) % 26
            res.append(
                chr(base + offset)
            )
        else:
            res.append(ch)
    return "".join(res)
\end{minted}
}"""
})

questions_data.append({
    "num": 50,
    "tema": "Tema 4: Strings, Fatiamento e Tuplas",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""No algoritmo oficial do Cadastro de Pessoas Físicas (CPF), o primeiro dígito verificador (o $10^\circ$ dígito) é calculado com base nos 9 primeiros dígitos:
1. Multiplica-se o $1^\circ$ dígito por 10, o $2^\circ$ por 9, o $3^\circ$ por 8, e assim por diante até o $9^\circ$ dígito multiplicado por 2.
2. Soma-se todos os 9 produtos parciais.
3. O resto da divisão dessa soma por 11 é calculado ($R = \text{soma} \pmod{11}$).
4. Se $R < 2$, o primeiro dígito verificador esperado é $0$; caso contrário, é $11 - R$.
Escreva uma função chamada \code{validar_primeiro_digito_cpf} que receba uma string de exatamente 11 dígitos numéricos e retorne \code{True} se o $10^\circ$ dígito estiver correto ou \code{False} caso contrário.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def validar_primeiro_digito_cpf(cpf_str: str) -> bool:}
    \item \textbf{Entrada:} \code{"12345678909"} | \textbf{Saída:} \code{True}
    \item \textbf{Entrada:} \code{"11144477705"} | \textbf{Saída:} \code{False}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def validar_primeiro_digito_cpf(
    cpf_str: str,
) -> bool:
    if (
        len(cpf_str) != 11
        or not cpf_str.isdigit()
    ):
        return False
    
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf_str[i]) * peso
        peso -= 1
        
    resto = soma % 11
    d_esp = (
        0 if resto < 2
        else 11 - resto
    )
    return int(cpf_str[9]) == d_esp
\end{minted}
}"""
})

# ==============================================================================
# TEMA 5: Listas, Mutabilidade e Matrizes (Q51 a Q60)
# ==============================================================================

questions_data.append({
    "num": 51,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Considere duas listas: \code{a = [1, 2]} e \code{b = [3, 4]}. Qual é a diferença fundamental entre executar \code{a.append(b)} e \code{a.extend(b)}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{a.append(b)} insere os elementos 3 e 4 individualmente no final de \code{a}, enquanto \code{a.extend(b)} cria uma cópia profunda.
    \item \code{a.append(b)} insere a lista \code{b} inteira como um único elemento no final de \code{a} (resultando em \code{[1, 2, [3, 4]]}), enquanto \code{a.extend(b)} itera sobre \code{b} e anexa cada elemento individualmente (resultando em \code{[1, 2, 3, 4]}).
    \item Não há nenhuma diferença prática; ambos os métodos resultam exatamente na lista \code{[1, 2, 3, 4]}.
    \item \code{a.extend(b)} só funciona para listas de strings, enquanto \code{a.append(b)} funciona para qualquer tipo.
    \item \code{a.append(b)} modifica \code{a} e retorna a nova lista, enquanto \code{a.extend(b)} não altera \code{a}.
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
* \code{list.append(obj)} adiciona o argumento exatamente como foi passado no final da lista. Se passarmos uma lista, ela vira um elemento aninhado (\code{[1, 2, [3, 4]]}).
* \code{list.extend(iterable)} itera sobre a coleção recebida e anexa cada um de seus elementos ao final da lista original (\code{[1, 2, 3, 4]}).
}"""
})

questions_data.append({
    "num": 52,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Analise o seguinte trecho de código em Python:
\begin{minted}{python}
matriz_original = [[1, 2], [3, 4]]
matriz_copia = matriz_original.copy()
matriz_copia[0][0] = 99
\end{minted}
Qual será o valor de \code{matriz_original[0][0]} após essa alteração?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item 1, pois \code{.copy()} cria uma cópia totalmente independente de todos os níveis.
    \item 99, pois \code{.copy()} realiza uma cópia rasa (\emph{shallow copy}), compartilhando as referências das sublistas internas.
    \item \code{None}, pois a lista original é limpa após a cópia.
    \item Ocorre um erro de execução (\code{TypeError}) na linha 3.
    \item 0.
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
O método \code{.copy()} (ou fatiamento \code{[:]}) cria uma cópia rasa (\emph{shallow copy}). Ele cria uma nova lista externa, mas os elementos internos (as sublistas) continuam sendo apontados para os mesmos endereços de memória. Para desacoplar completamente estruturas aninhadas, é obrigatório utilizar \code{copy.deepcopy()}.
}"""
})

questions_data.append({
    "num": 53,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Qual das seguintes expressões em Python utiliza corretamente Compreensão de Listas (\emph{List Comprehension}) para criar uma lista com o quadrado apenas dos números ímpares presentes na lista \code{numeros = [1, 2, 3, 4, 5, 6]}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{[x ** 2 for x in numeros if x % 2 != 0]}
    \item \code{[for x in numeros if x % 2 != 0: x ** 2]}
    \item \code{[x ** 2 if x % 2 != 0 for x in numeros]}
    \item \code{[x * 2 for x in numeros while x % 2 != 0]}
    \item \code{list(x ** 2 for x in numeros and x % 2 != 0)}
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (A)}

\textbf{Justificativa:}
A sintaxe canônica de list comprehension com filtro condicional é:\\
\code{[expressao_retorno for item in iteravel if condicao_filtro]}.\\
Logo, \code{[x ** 2 for x in numeros if x % 2 != 0]} produz \code{[1, 9, 25]}.
}"""
})

questions_data.append({
    "num": 54,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Um sistema de controle de vendas recebeu uma lista de preços com algumas entradas corrompidas contendo valores negativos ou iguais a zero. Escreva uma função chamada \code{limpar_precos_invalidos} que receba uma lista de preços em ponto flutuante e retorne uma nova lista contendo apenas os preços estritamente positivos ($> 0.0$).

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List}\\\code{def limpar_precos_invalidos(precos: List[float]) -> List[float]:}
    \item \textbf{Entrada:} \code{[29.9, -5.0, 0.0, 45.5, 12.0]} | \textbf{Saída:} \code{[29.9, 45.5, 12.0]}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List

def limpar_precos_invalidos(
    precos: List[float]
) -> List[float]:
    return [p for p in precos if p > 0.0]
\end{minted}
}"""
})

questions_data.append({
    "num": 55,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Em uma competição esportiva, a nota de um competidor é calculada descartando apenas uma ocorrência da menor nota e uma ocorrência da maior nota atribuída pelos jurados, e calculando a média aritmética das notas restantes. Escreva uma função chamada \code{media_sem_extremos} que receba uma lista com pelo menos 3 notas e retorne a média aparada resultante.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List}\\\code{def media_sem_extremos(notas: List[float]) -> float:}
    \item \textbf{Entrada:} \code{[8.5, 9.0, 6.0, 10.0, 7.5]} | \textbf{Saída:} \code{8.333333333333334}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List

def media_sem_extremos(
    notas: List[float],
) -> float:
    ord_n = sorted(notas)
    miolo = ord_n[1:-1]
    return sum(miolo) / len(miolo)
\end{minted}
}"""
})

questions_data.append({
    "num": 56,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{intercalar_listas} que receba duas listas de mesmo comprimento (\code{fila_a} e \code{fila_b}) e retorne uma nova lista contendo os elementos intercalados alternadamente (o primeiro de A, depois o primeiro de B, o segundo de A, o segundo de B, e assim por diante).

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List}\\\code{def intercalar_listas(fila_a: List[str], fila_b: List[str]) -> List[str]:}
    \item \textbf{Entrada:} \code{["Ana", "Carlos"], ["Bia", "Daniel"]}
    \item \textbf{Saída:} \code{["Ana", "Bia", "Carlos", "Daniel"]}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List

def intercalar_listas(
    fila_a: List[str],
    fila_b: List[str],
) -> List[str]:
    resultado = []
    for a, b in zip(fila_a, fila_b):
        resultado.append(a)
        resultado.append(b)
    return resultado
\end{minted}
}"""
})

questions_data.append({
    "num": 57,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{trocar_pares_adjacentes} que receba uma lista de inteiros com quantidade par de elementos e retorne uma nova lista na qual as posições dos pares vizinhos estejam invertidas: o elemento no índice 0 troca com o índice 1, o elemento no índice 2 troca com o índice 3, e assim por diante.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List}\\\code{def trocar_pares_adjacentes(lista_itens: List[int]) -> List[int]:}
    \item \textbf{Entrada:} \code{[10, 20, 30, 40]} | \textbf{Saída:} \code{[20, 10, 40, 30]}
    \item \textbf{Entrada:} \code{[1, 2, 3, 4, 5, 6]} | \textbf{Saída:} \code{[2, 1, 4, 3, 6, 5]}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List

def trocar_pares_adjacentes(
    lista_itens: List[int],
) -> List[int]:
    res = list(lista_itens)
    for i in range(0, len(res), 2):
        res[i], res[i + 1] = (
            res[i + 1],
            res[i],
        )
    return res
\end{minted}
}"""
})

questions_data.append({
    "num": 58,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Uma imagem digital monocromática é representada por uma matriz bidimensional de dimensões $M \times N$ (uma lista de $M$ listas, cada uma com $N$ inteiros correspondentes aos tons de cinza). A rotação e transposição dessa imagem exige converter as linhas em colunas. Escreva uma função chamada \code{transpor_imagem} que receba essa matriz e retorne a matriz transposta de dimensão $N \times M$.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List}\\\code{def transpor_imagem(matriz_pixels: List[List[int]]) -> List[List[int]]:}
    \item \textbf{Entrada:} \code{[[1, 2, 3], [4, 5, 6]]} | \textbf{Saída:} \code{[[1, 4], [2, 5], [3, 6]]}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List

def transpor_imagem(
    matriz_pixels: List[List[int]],
) -> List[List[int]]:
    if not matriz_pixels:
        return []
    n_lin = len(matriz_pixels)
    n_col = len(matriz_pixels[0])
    
    transposta = []
    for c in range(n_col):
        nova_linha = []
        for l in range(n_lin):
            val = matriz_pixels[l][c]
            nova_linha.append(val)
        transposta.append(nova_linha)
    return transposta
\end{minted}
}"""
})

questions_data.append({
    "num": 59,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Uma rede de lojas armazena em uma matriz as quantidades de produtos vendidos em cada filial (cada linha representa uma filial e cada coluna um tipo de produto). Um vetor unidimensional armazena o preço unitário de cada produto. Escreva uma função chamada \code{faturamento_por_departamento} que realize a multiplicação da matriz de vendas pelo vetor de preços, retornando uma lista com o faturamento total arrecadado por cada filial.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List}\\\code{def faturamento_por_departamento(}\\\code{    matriz_vendas: List[List[float]],}\\\code{    vetor_precos: List[float]}\\\code{) -> List[float]:}
    \item \textbf{Entrada:} \code{[[2.0, 1.0], [0.0, 3.0]], [10.0, 20.0]} | \textbf{Saída:} \code{[40.0, 60.0]}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List

def faturamento_por_departamento(
    matriz_vendas: List[List[float]],
    vetor_precos: List[float],
) -> List[float]:
    faturamentos = []
    for linha in matriz_vendas:
        parcial = [
            q * p
            for q, p in zip(
                linha, vetor_precos
            )
        ]
        faturamentos.append(
            sum(parcial)
        )
    return faturamentos
\end{minted}
}"""
})

questions_data.append({
    "num": 60,
    "tema": "Tema 5: Listas, Mutabilidade e Matrizes",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""No mercado financeiro, a Média Móvel Simples é muito utilizada para suavizar oscilações diárias de preços. Dada uma lista de preços históricos de uma ação e um tamanho de janela $K$ ($K \ge 1$), a média móvel no dia $i$ é a média aritmética dos $K$ valores compreendidos entre o dia $i - K + 1$ e o dia $i$. Escreva uma função chamada \code{calcular_media_movel} que receba a lista de preços e a janela $K$, e retorne uma lista contendo as médias móveis calculadas a partir do momento em que a primeira janela completa estiver disponível.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List}\\\code{def calcular_media_movel(precos_diarios: List[float], tamanho_janela: int) -> List[float]:}
    \item \textbf{Entrada:} \code{[100.0, 102.0, 104.0, 106.0, 108.0], 3} | \textbf{Saída:} \code{[102.0, 104.0, 106.0]}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List

def calcular_media_movel(
    precos_diarios: List[float],
    tamanho_janela: int,
) -> List[float]:
    if (
        len(precos_diarios)
        < tamanho_janela
    ):
        return []
    medias = []
    n = (
        len(precos_diarios)
        - tamanho_janela
        + 1
    )
    for i in range(n):
        janela = precos_diarios[
            i : i + tamanho_janela
        ]
        val = (
            sum(janela)
            / tamanho_janela
        )
        medias.append(val)
    return medias
\end{minted}
}"""
})

# ==============================================================================
# TEMA 6: Dicionários e Conjuntos (dict e set) (Q61 a Q70)
# ==============================================================================


questions_data.append({
    "num": 63,
    "tema": "Tema 6: Dicionários e Conjuntos (dict e set)",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Dado o dicionário \code{precos = {"arroz": 5.50, "feijao": 8.00}}, qual é a forma segura de consultar o preço do item \code{"batata"} sem provocar uma exceção de erro do tipo \code{KeyError} caso ele não esteja cadastrado?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{precos["batata"]}
    \item \code{precos.get("batata", 0.0)}
    \item \code{precos.pop("batata")}
    \item \code{precos.find("batata")}
    \item \code{precos.search("batata")}
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
O método \code{dict.get(chave, valor_padrao)} retorna o valor associado à chave se ela existir no dicionário, ou o valor padrão (no caso, \code{0.0}) se a chave não for encontrada, evitando o lançamento do erro \code{KeyError}.
}"""
})

questions_data.append({
    "num": 64,
    "tema": "Tema 6: Dicionários e Conjuntos (dict e set)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{contar_frequencia_palavras} que receba uma string contendo um texto em minúsculas com palavras separadas por espaços e retorne um dicionário no qual cada chave é uma palavra e o valor correspondente é a quantidade de vezes que ela apareceu no texto.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Dict}\\\code{def contar_frequencia_palavras(texto: str) -> Dict[str, int]:}
    \item \textbf{Entrada:} \code{"otimo produto produto excelente otimo produto"}
    \item \textbf{Saída:} \code{{"otimo": 2, "produto": 3, "excelente": 1}}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Dict

def contar_frequencia_palavras(
    texto: str,
) -> Dict[str, int]:
    palavras = texto.strip().split()
    contagens: Dict[str, int] = {}
    for p in palavras:
        contagens[p] = (
            contagens.get(p, 0) + 1
        )
    return contagens
\end{minted}
}"""
})


questions_data.append({
    "num": 66,
    "tema": "Tema 6: Dicionários e Conjuntos (dict e set)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{inverter_dicionario} que receba um dicionário cujas chaves e valores sejam strings (assumindo que todos os valores são distintos) e retorne um novo dicionário no qual as chaves originais tornam-se valores e os valores tornam-se as novas chaves.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Dict}\\\code{def inverter_dicionario(dicionario_original: Dict[str, str]) -> Dict[str, str]:}
    \item \textbf{Entrada:} \code{{"BR": "Brasil", "FR": "Franca"}}
    \item \textbf{Saída:} \code{{"Brasil": "BR", "Franca": "FR"}}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Dict

def inverter_dicionario(
    dicionario_original: Dict[str, str],
) -> Dict[str, str]:
    return {
        v: k
        for k, v in (
            dicionario_original.items()
        )
    }
\end{minted}
}"""
})

questions_data.append({
    "num": 67,
    "tema": "Tema 6: Dicionários e Conjuntos (dict e set)",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Um catálogo de supermercado possui itens cadastrados em uma lista de tuplas no formato \code{(nome_produto, categoria)}. Escreva uma função chamada \code{agrupar_por_categoria} que receba essa lista e retorne um dicionário no qual cada chave é o nome de uma categoria e o valor é a lista de produtos pertencentes àquela categoria.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List, Tuple, Dict}\\\code{def agrupar_por_categoria(}\\\code{    itens: List[Tuple[str, str]]}\\\code{) -> Dict[str, List[str]]:}
    \item \textbf{Entrada:} \\\code{[("Arroz", "Alimentos"), ("Sabonete", "Higiene"), ("Feijao", "Alimentos")]}
    \item \textbf{Saída:} \\\code{{"Alimentos": ["Arroz", "Feijao"], "Higiene": ["Sabonete"]}}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List, Tuple, Dict

def agrupar_por_categoria(
    itens: List[Tuple[str, str]]
) -> Dict[str, List[str]]:
    agrupado: Dict[str, List[str]] = {}
    for produto, categoria in itens:
        if categoria not in agrupado:
            agrupado[categoria] = []
        agrupado[categoria].append(produto)
    return agrupado
\end{minted}
}"""
})

questions_data.append({
    "num": 68,
    "tema": "Tema 6: Dicionários e Conjuntos (dict e set)",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Duas filiais de uma rede de lojas precisam consolidar seus estoques ao final do expediente. Cada estoque é representado por um dicionário no formato \code{{"produto": quantidade}}. Escreva uma função chamada \code{consolidar_estoques} que receba os dois dicionários e retorne um novo dicionário consolidado contendo a soma das quantidades para produtos que existirem em ambas as lojas, e a quantidade original para os produtos exclusivos de uma única loja.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import Dict}\\\code{def consolidar_estoques(}\\\code{    estoque_loja1: Dict[str, int],}\\\code{    estoque_loja2: Dict[str, int]}\\\code{) -> Dict[str, int]:}
    \item \textbf{Entrada:} \code{{"Camisa": 10, "Calca": 5}, {"Camisa": 8, "Tenis": 3}}
    \item \textbf{Saída:} \code{{"Camisa": 18, "Calca": 5, "Tenis": 3}}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Dict

def consolidar_estoques(
    estoque_loja1: Dict[str, int],
    estoque_loja2: Dict[str, int]
) -> Dict[str, int]:
    consolidado = dict(estoque_loja1)
    for prod, qtd in estoque_loja2.items():
        consolidado[prod] = (
            consolidado.get(prod, 0) + qtd
        )
    return consolidado
\end{minted}
}"""
})


# ==============================================================================
# TEMA 7: Programação Orientada a Objetos e Manipulação de Arquivos (Q71 a Q80)
# ==============================================================================

questions_data.append({
    "num": 71,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Em Programação Orientada a Objetos em Python, qual é o papel do primeiro parâmetro \code{self} na definição dos métodos de instância dentro de uma classe?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item \code{self} é uma palavra-chave reservada que faz referência direta à classe mãe (superclasse).
    \item \code{self} representa a instância específica do objeto que está invocando o método, permitindo acessar e manipular seus atributos e outros métodos.
    \item \code{self} serve exclusivamente para definir variáveis estáticas compartilhadas entre todas as instâncias da classe.
    \item O uso de \code{self} é opcional e pode ser substituído pela palavra-chave \code{global} para criar atributos públicos.
    \item \code{self} é o nome do método construtor padrão executado para alocar memória ao objeto.
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
Em Python, o parâmetro \code{self} referencia explicitamente a instância atual do objeto em tempo de execução. Ao chamar um método em um objeto (\code{obj.metodo()}), o Python passa automaticamente a própria instância como primeiro argumento (\code{Classe.metodo(obj)}), permitindo ao método inspecionar e alterar os atributos e o estado daquele objeto.
}"""
})

questions_data.append({
    "num": 72,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Fácil",
    "tipo": "Múltipla Escolha",
    "enunciado": r"""Por que a comunidade de desenvolvedores Python recomenda fortemente o uso do gerenciador de contexto \code{with open(...) as f:} ao invés de usar \code{f = open(...)} seguido de \code{f.close()}?

\begin{enumerate}[label=\textbf{(\Alph*)}]
    \item Porque a instrução \code{with} lê o arquivo de forma assíncrona mais rápida.
    \item Porque o gerenciador de contexto \code{with} garante o fechamento automático e a liberação dos recursos do arquivo no sistema operacional, mesmo se ocorrer uma exceção ou erro durante o processamento.
    \item Porque a função \code{open()} tradicional é considerada obsoleta no Python 3.
    \item Porque arquivos abertos com \code{with} não ocupam memória RAM.
    \item Porque o \code{with} converte automaticamente o arquivo de texto para formato binário criptografado.
\end{enumerate}""",
    "resposta": r"""\ifmostrarGabarito{
\textbf{Resposta: (B)}

\textbf{Justificativa:}
A estrutura \code{with} invoca internamente os métodos de gerenciamento de contexto (\code{__enter__} e \code{__exit__}). Isso assegura que o descritor de arquivo seja fechado adequadamente logo após a saída do bloco, mesmo que ocorra uma exceção não tratada dentro dele.
}"""
})


questions_data.append({
    "num": 74,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Implemente uma classe chamada \code{Livro} que represente um exemplar de leitura de uma biblioteca com os seguintes requisitos:
1. Construtor \code{__init__(self, titulo: str, autor: str, total_paginas: int)} que inicialize os atributos e crie o atributo \code{paginas_lidas: int} iniciado em $0$.
2. Método \code{ler_paginas(self, quantidade: int) -> int} que adicione a quantidade lida a \code{paginas_lidas} (sem ultrapassar \code{total_paginas}) e retorne quantas páginas ainda faltam para concluir o livro.
3. Método \code{print(self) -> None} que exiba na tela a mensagem formatada: \code{"'TITULO' por AUTOR (Lidas: X/TOTAL)"}.

\textbf{Exemplo de Uso:}
\begin{minted}{python}
livro = Livro("1984", "George Orwell", 300)
faltam = livro.ler_paginas(50)  # retorna 250
livro.print()  # exibe: '1984' por George Orwell (Lidas: 50/300)
\end{minted}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
class Livro:
    def __init__(
        self,
        titulo: str,
        autor: str,
        total_paginas: int,
    ) -> None:
        self.titulo: str = titulo
        self.autor: str = autor
        self.total_paginas: int = (
            total_paginas
        )
        self.paginas_lidas: int = 0

    def ler_paginas(
        self, quantidade: int
    ) -> int:
        self.paginas_lidas = min(
            self.total_paginas,
            self.paginas_lidas + quantidade,
        )
        return (
            self.total_paginas
            - self.paginas_lidas
        )

    def print(self) -> None:
        print(
            f"'{self.titulo}' por "
            f"{self.autor} (Lidas: "
            f"{self.paginas_lidas}/"
            f"{self.total_paginas})"
        )
\end{minted}
}"""
})

questions_data.append({
    "num": 75,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{contar_erros_log} que receba o caminho de um arquivo de texto \code{.txt} de log de uma aplicação web. Utilizando o gerenciador de contexto \code{with}, a função deve abrir o arquivo no modo leitura (\code{'r'}), percorrer todas as linhas e contar quantas contêm a palavra \code{"ERROR"} (em maiúsculas), retornando essa contagem como um número inteiro.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{def contar_erros_log(caminho_arquivo: str) -> int:}
    \item \textbf{Entrada:} \code{"servidor.log"} (arquivo contendo 5 ocorrências de \code{"ERROR"})
    \item \textbf{Saída:} \code{5}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
def contar_erros_log(
    caminho_arquivo: str,
) -> int:
    total_erros = 0
    with open(
        caminho_arquivo,
        "r",
        encoding="utf-8",
    ) as arq:
        for linha in arq:
            if "ERROR" in linha:
                total_erros += 1
    return total_erros
\end{minted}
}"""
})

questions_data.append({
    "num": 76,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Escreva uma função chamada \code{salvar_produtos_csv} que receba o caminho de um arquivo de saída e uma lista de tuplas contendo \code{(nome_produto: str, preco: float)}. A função deve utilizar a cláusula \code{with} no modo de escrita (\code{'w'}) para gravar um arquivo CSV com cabeçalho \code{"produto,preco"} e cada item em uma nova linha com o preço formatado em duas casas decimais, retornando \code{True} após finalizar a gravação.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List, Tuple}\\\code{def salvar_produtos_csv(caminho_arquivo: str, produtos: List[Tuple[str, float]]) -> bool:}
    \item \textbf{Entrada:} \code{"precos.csv", [("Mouse", 80.0), ("Teclado", 150.0)]}
    \item \textbf{Saída:} \code{True} (e o arquivo \code{"precos.csv"} salvo no disco)
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List, Tuple

def salvar_produtos_csv(
    caminho_arquivo: str,
    produtos: List[Tuple[str, float]],
) -> bool:
    with open(
        caminho_arquivo,
        "w",
        encoding="utf-8",
    ) as arq:
        arq.write("produto,preco\n")
        for nome, preco in produtos:
            arq.write(
                f"{nome},{preco:.2f}\n"
            )
    return True
\end{minted}
}"""
})

questions_data.append({
    "num": 77,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Fácil",
    "tipo": "Código",
    "enunciado": r"""Implemente uma classe chamada \code{ContaBancaria} que gerencie o saldo de um cliente com os seguintes métodos e atributos:
1. Construtor \code{__init__(self, titular: str, saldo_inicial: float = 0.0)} que inicialize o titular e o saldo da conta.
2. Método \code{depositar(self, valor: float) -> float} que adicione o valor ao saldo (se o valor for positivo) e retorne o novo saldo atualizado.
3. Método \code{sacar(self, valor: float) -> bool} que debite o valor do saldo se houver saldo suficiente ($saldo \ge valor$ e $valor > 0$) retornando \code{True}. Caso contrário, não altera o saldo e retorna \code{False}.
4. Método \code{print(self) -> None} que exiba na tela a mensagem formatada: \code{"Conta de TITULAR - Saldo: R\$ X.XX"}.

\textbf{Exemplo de Uso:}
\begin{minted}{python}
conta = ContaBancaria("Maria", 100.0)
conta.depositar(50.0)  # Saldo: 150.0
sucesso = conta.sacar(200.0)  # Retorna False (saldo insuficiente)
conta.print()  # Exibe: Conta de Maria - Saldo: R$ 150.00
\end{minted}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
class ContaBancaria:
    def __init__(
        self,
        titular: str,
        saldo_inicial: float = 0.0
    ) -> None:
        self.titular: str = titular
        self.saldo: float = saldo_inicial

    def depositar(self, valor: float) -> float:
        if valor > 0:
            self.saldo += valor
        return self.saldo

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def print(self) -> None:
        print(
            f"Conta de {self.titular} - "
            f"Saldo: R$ {self.saldo:.2f}"
        )
\end{minted}
}"""
})

questions_data.append({
    "num": 78,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Modele uma hierarquia de classes para uma concessionária de veículos:
1. Superclasse \code{Veiculo}:
   * Construtor \code{__init__(self, marca: str, modelo: str, preco: float)}.
   * Método \code{exibir_ficha(self) -> str} que retorne \code{"MARCA MODELO - R$ PRECO"}.
2. Subclasse \code{CarroEletrico} (que herda de \code{Veiculo}):
   * Construtor \code{__init__(self, marca: str, modelo: str, preco: float, capacidade_kwh: float)} utilizando \code{super()} para os atributos herdados.
   * Método \code{estimar_autonomia(self, consumo_kwh_por_km: float) -> float} que retorne o alcance estimado em km ($\frac{\text{capacidade\_kwh}}{\text{consumo\_kwh\_por\_km}}$).

\textbf{Exemplo de Uso:}
\begin{minted}{python}
carro = CarroEletrico(
    "Tesla", "Model 3", 280000.0, 75.0
)
# Ficha: Tesla Model 3 - R$ 280000.00
print(carro.exibir_ficha())
# Autonomia estimada: 500.0 km
autonomia = carro.estimar_autonomia(0.15)
\end{minted}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
class Veiculo:
    def __init__(
        self,
        marca: str,
        modelo: str,
        preco: float
    ) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.preco: float = preco

        def exibir_ficha(self) -> str:
        return (
            f"{self.marca} {self.modelo} - "
            f"R$ {self.preco:.2f}"
        )

class CarroEletrico(Veiculo):
    def __init__(
        self,
        marca: str,
        modelo: str,
        preco: float,
        capacidade_kwh: float,
    ) -> None:
        super().__init__(
            marca, modelo, preco
        )
        self.capacidade_kwh: float = (
            capacidade_kwh
        )

    def estimar_autonomia(
        self,
        consumo_kwh_por_km: float,
    ) -> float:
        return (
            self.capacidade_kwh
            / consumo_kwh_por_km
        )
\end{minted}
}"""
})

questions_data.append({
    "num": 79,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Médio",
    "tipo": "Código",
    "enunciado": r"""Uma plataforma de e-commerce mantém seus pedidos salvos em um arquivo CSV formatado com cabeçalho:
\begin{verbatim}
id,cliente,valor
1,Maria Silva,120.50
2,Joao Souza,45.00
\end{verbatim}
Escreva uma função chamada \code{carregar_pedidos_csv} que leia o arquivo informado via parâmetro usando \code{with} e retorne uma lista de dicionários tipados no formato \code{[{"id": int, "cliente": str, "valor": float}]}. Linhas em branco devem ser ignoradas.

\begin{itemize}[leftmargin=*]
    \item \textbf{Protótipo:}\newline \code{from typing import List, Dict, Union}\\\code{def carregar_pedidos_csv(}\\\code{    caminho_csv: str}\\\code{) -> List[Dict[str, Union[int, str, float]]]:}
    \item \textbf{Entrada:} \code{"pedidos.csv"}
    \item \textbf{Saída:} \\\code{[{"id": 1, "cliente": "Maria Silva", "valor": 120.50}, {"id": 2, "cliente": "Joao Souza", "valor": 45.00}]}
\end{itemize}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import List, Dict, Union

def carregar_pedidos_csv(
    caminho_csv: str,
) -> List[Dict[str, Union[int, str, float]]]:
    pedidos: List[
        Dict[str, Union[int, str, float]]
    ] = []
    with open(
        caminho_csv, "r", encoding="utf-8"
    ) as arq:
        linhas = arq.readlines()
        if not linhas:
            return []
        # Ignora cabecalho
        for linha in linhas[1:]:
            limpa = linha.strip()
            if not limpa:
                continue
            partes = limpa.split(",")
            pedidos.append({
                "id": int(partes[0]),
                "cliente": partes[1],
                "valor": float(partes[2]),
            })
    return pedidos
\end{minted}
}"""
})

questions_data.append({
    "num": 80,
    "tema": "Tema 7: Programação Orientada a Objetos e Manipulação de Arquivos",
    "nivel": "Difícil",
    "tipo": "Código",
    "enunciado": r"""Desenvolva um sistema completo de controle de acervo para uma biblioteca comunitária criando a classe \code{Biblioteca}:
\begin{enumerate}
    \item Construtor \code{__init__(self, nome_biblioteca: str)}: inicializa o nome e o catálogo interno \code{self.catalogo: Dict[int, Dict[str, Union[str, int]]]}.
    \item Método \code{cadastrar_livro(self, livro_id: int,}\\\code{    titulo: str, quantidade: int) -> None}: adiciona ou atualiza os dados do livro no catálogo.
    \item Método \code{emprestar_livro(self, livro_id: int) -> bool}: se o livro existir e possuir quantidade disponível ($> 0$), decrementa em 1 unidade e retorna \code{True}. Caso contrário, retorna \code{False}.
    \item Método \code{exportar_inventario(self, caminho_txt: str) -> bool}: grava um arquivo de texto com a lista de todos os livros no formato \code{"[ID] TITULO - QTD exemplares"} e encerra com a linha final \code{"Total de titulos: N"}, retornando \code{True}.
\end{enumerate}

\textbf{Exemplo de Uso:}
\begin{minted}{python}
bib = Biblioteca("Biblioteca Central")
bib.cadastrar_livro(101, "Dom Casmurro", 3)
# Empresta: qtd vira 2, retorna True
bib.emprestar_livro(101)
# Grava inventario no disco
bib.exportar_inventario("inventario.txt")
\end{minted}""",
    "resposta": r"""\ifmostrarGabarito{
\begin{minted}{python}
from typing import Dict, Union

class Biblioteca:
    def __init__(
        self, nome_biblioteca: str
    ) -> None:
        self.nome_biblioteca: str = (
            nome_biblioteca
        )
        self.catalogo: Dict[
            int, Dict[str, Union[str, int]]
        ] = {}

    def cadastrar_livro(
        self,
        livro_id: int,
        titulo: str,
        quantidade: int,
    ) -> None:
        self.catalogo[livro_id] = {
            "titulo": titulo,
            "quantidade": quantidade,
        }

    def emprestar_livro(
        self, livro_id: int
    ) -> bool:
        cat = self.catalogo
        if (
            livro_id in cat
            and int(cat[livro_id]["quantidade"]) > 0
        ):
            qtd = int(cat[livro_id]["quantidade"])
            cat[livro_id]["quantidade"] = (
                qtd - 1
            )
            return True
        return False

    def exportar_inventario(
        self, caminho_txt: str
    ) -> bool:
        with open(
            caminho_txt,
            "w",
            encoding="utf-8",
        ) as arq:
            for l_id, d in self.catalogo.items():
                tit = d["titulo"]
                qtd = d["quantidade"]
                arq.write(
                    f"[{l_id}] {tit} - "
                    f"{qtd} exemplares\n"
                )
            n_tot = len(self.catalogo)
            arq.write(
                f"Total de titulos: {n_tot}\n"
            )
        return True
\end{minted}
}"""
})

# ==============================================================================
# GERAÇÃO DOS ARQUIVOS DE RESPOSTA E DO MAIN.TEX
# ==============================================================================

print(f"Total de questões configuradas: {len(questions_data)}")

import re

def escape_code_blocks(text: str) -> str:
    result = []
    i = 0
    while i < len(text):
        if text.startswith(r"\code{", i):
            result.append(r"\code{")
            i += 6
            depth = 1
            inner = []
            while i < len(text) and depth > 0:
                if text[i] == "{" and (i == 0 or text[i-1] != "\\"):
                    depth += 1
                    inner.append(r"\{")
                elif text[i] == "}" and (i == 0 or text[i-1] != "\\"):
                    depth -= 1
                    if depth == 0:
                        break
                    inner.append(r"\}")
                elif text[i] == "_" and (i == 0 or text[i-1] != "\\"):
                    inner.append(r"\_")
                elif text[i] == "$" and (i == 0 or text[i-1] != "\\"):
                    inner.append(r"\$")
                elif text[i] == "&" and (i == 0 or text[i-1] != "\\"):
                    inner.append(r"\&")
                else:
                    inner.append(text[i])
                i += 1
            result.append("".join(inner))
            result.append("}")
            if i < len(text) and text[i] == "}":
                i += 1
        else:
            result.append(text[i])
            i += 1
    return "".join(result)

def sanitize_latex(text: str) -> str:
    # 1. Escape special characters inside \code{...}
    text = escape_code_blocks(text)
    
    # 2. Replace markdown bold with LaTeX \textbf{...}
    text = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", text)

    # 3. Escape % in regular text when not inside minted or math
    parts = re.split(r"(\\begin\{minted\}\{python\}.*?\\end\{minted\})", text, flags=re.DOTALL)
    for idx, part in enumerate(parts):
        if not part.startswith(r"\begin{minted}"):
            # Replace unescaped % with \%
            parts[idx] = re.sub(r"(?<!\\)%(?![a-zA-Z])", r"\\%", part)
    text = "".join(parts)
    return text

# Renumerar todas as questões consecutivamente
for idx, q in enumerate(questions_data, start=1):
    q["num"] = idx

# 1. Limpar e recriar o diretório answers/
import shutil
if os.path.exists(ANSWERS_DIR):
    shutil.rmtree(ANSWERS_DIR)
os.makedirs(ANSWERS_DIR, exist_ok=True)

# 2. Salvar os arquivos em answers/
for q in questions_data:
    ans_path = os.path.join(ANSWERS_DIR, f"Q{q['num']}.tex")
    resp_text = q["resposta"].strip()
    if resp_text.startswith(r"\ifmostrarGabarito{") and resp_text.endswith("}"):
        resp_text = r"\ifmostrarGabarito" + resp_text[len(r"\ifmostrarGabarito{"):-1] + "\n\\fi"
    if r"\begin{minted}" not in resp_text:
        resp_text = sanitize_latex(resp_text)
    with open(ans_path, "w", encoding="utf-8") as f:
        f.write(resp_text + "\n")

# 3. Gerar o main.tex da Lista 11
main_tex_content = []
main_tex_content.append(r"""\vspace{0.5cm}

\noindent \textbf{\Large Lista de Exercícios 11 — Revisão Geral do Curso}

\vspace{0.3cm}
\noindent \textbf{Orientações e Instruções Gerais:}
\begin{itemize}[leftmargin=*]
    \item Esta lista consolida os tópicos fundamentais ministrados ao longo de toda a disciplina, totalizando \textbf{100,0 pontos}.
    \item \textbf{Formato e Entrega:} As resoluções devem ser desenvolvidas e entregues em formato Jupyter Notebook (\texttt{.ipynb}) ou Google Colab na plataforma Google Classroom, na tarefa designada e impreterivelmente até o dia e horário determinados.
    \item Para questões de implementação de código, utilize os nomes de funções, assinaturas e \textbf{Type Hints} estritamente conforme especificado nos protótipos.
    \item Respeite as restrições específicas de cada tema (ex: não usar laços no Tema 1 ou no Tema 2).
    \item A pontuação de cada questão é atribuída de acordo com seu nível: \textbf{Fácil (1,0 ponto)}, \textbf{Médio (1,8 ponto)} e \textbf{Difícil (3,0 pontos)}.
\end{itemize}

\vspace{0.5cm}
""")

PONTOS_POR_NIVEL = {
    "Fácil": "1,0 ponto",
    "Médio": "1,8 ponto",
    "Difícil": "3,0 pontos",
}

current_tema = ""
is_first = True

for q in questions_data:
    if q["tema"] != current_tema:
        if not is_first:
            main_tex_content.append(r"\end{enumerate}" + "\n")
        current_tema = q["tema"]
        main_tex_content.append(f"\n\\section*{{{current_tema}}}\n")
        main_tex_content.append(f"\\begin{{enumerate}}[label=\\textbf{{Q\\arabic*.}}, start={q['num']}]\n")
        is_first = False
    
    pts_str = PONTOS_POR_NIVEL[q["nivel"]]
    tipo_str = " - Múltipla Escolha" if q["tipo"] == "Múltipla Escolha" else ""
    label_nivel = f"\\textbf{{[{q['nivel']}{tipo_str} - {pts_str}]}}"
    enunciado_sanitizado = sanitize_latex(q["enunciado"])
    main_tex_content.append(f"\\item {label_nivel} {enunciado_sanitizado}\n")
    main_tex_content.append(f"\\input{{body/Lista_11/answers/Q{q['num']}}}\n")
    main_tex_content.append(r"\vspace{0.4cm}" + "\n")

main_tex_content.append(r"\end{enumerate}")

main_path = os.path.join(BASE_DIR, "main.tex")
with open(main_path, "w", encoding="utf-8") as f:
    f.write("\n".join(main_tex_content))

print(f"Lista 11 gerada com sucesso em: {main_path}")

