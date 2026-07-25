# ⚓ Marinha do Brasil
## Centro de Instrução Almirante Alexandrino (CIAA)
### Departamento de Aperfeiçoamento Avançado para Oficiais

---

# 🎓 Revisão Acelerada de Programação (RAP) — RAP-2026
**Curso de Aperfeiçoamento Avançado em Guerra Acústica (C-ApA-Of-GA)**

Este repositório contém o material didático, os códigos-fonte e os exercícios práticos da disciplina **Revisão Acelerada de Programação (RAP)**, desenvolvida sob a perspectiva da **Guerra Acústica** para instrução de Oficiais da Marinha do Brasil.

---

## 🎯 Propósito e Objetivos da Disciplina

A disciplina tem por finalidade consolidar os conceitos fundamentais de lógica de programação e o desenvolvimento de algoritmos utilizando a linguagem Python. O conteúdo é estruturado de forma intensiva, visando capacitar os oficiais nas seguintes competências técnicas e operacionais:

*   **Manipulação de Dados Complexos**: Tratamento e estruturação de dados de sensores e séries temporais.
*   **Automação de Rotinas de Análise**: Desenvolvimento de rotinas automatizadas para otimização de fluxos de trabalho militares.
*   **Implementação de Soluções Computacionais Aplicadas**: Criação rápida de algoritmos e scripts voltados à Guerra Acústica, fornecendo suporte técnico-operacional e garantindo maior celeridade no cumprimento de tarefas correlatas à especialidade.

---

## 📋 Conteúdo Programático (Planejamento de Aulas)

A ementa da disciplina está organizada nas seguintes sessões:

| Aula | Conteúdo Programático |
| :---: | :--- |
| **01** | Apresentação da Disciplina, Introdução ao Python, Docker, Jupyter Lab e IDE (VS Code). |
| **02** | Variáveis, Tipos Primitivos, Conversão de Tipos (*Casting*), Funções Integradas (*Built-ins*), Condicionais e Introdução a Funções. |
| **03** | Estruturas de Repetição (`for` e `while`) e Controle de Fluxo (`break` e `continue`). |
| **04** | Estruturas de Dados Dinâmicas: Listas, Matrizes e Métodos Principais (`append`, `insert`, `remove`). |
| **05** | Atividades Práticas Dirigidas. |
| **06** | Manipulação de Cadeias de Caracteres (*Strings*), Fatiamento e Métodos de Busca/Validação. |
| **07** | Atividades Práticas Dirigidas. |
| **08** | Estruturas de Dados de Associação: Dicionários, Métodos de Busca e Análise de Complexidade. |
| **09** | Estruturas de Dados Estáticas: Tuplas, Imutabilidade e Desempacotamento de Variáveis (*Unpacking*). |
| **10** | Entrada e Saída de Dados (I/O): Gerenciamento de Contexto (`with`), Leitura/Escrita de Arquivos (TXT, CSV, JSON) e Módulos `os`/`pathlib`. |
| **11** | Funções Avançadas: Escopo de Variáveis (Global vs Local), Parâmetros Opcionais, Empacotamento (`*args`/`**kwargs`) e Tipagem. |
| **12** | Atividades Práticas Dirigidas. |
| **13** | Paradigma de Orientação a Objetos (POO): Classes, Atributos, Construtores, Herança e Sobrescrita de Métodos. |
| **14** | Atividades Práticas Dirigidas. |
| **15** | **Prova Escrita Individual (PI)** e Entrega da Primeira Lista de Exercícios (L1). |
| **16** | Resolução da Primeira Lista de Exercícios (L1). |
| **17** | Introdução à Visualização de Dados: Arquitetura do `Matplotlib`, Gráficos Bidimensionais e Customização de Elementos. |
| **18** | Computação Numérica de Alto Desempenho com `NumPy`: Arrays, Operações Vetorizadas e Álgebra Linear. |
| **19** | Análise de Dados com `Pandas`: Estruturas `Series` e `DataFrame`, Leitura de CSVs, Seleção/Filtragem e Agrupamentos (`groupby`). |
| **20** | Atividades Práticas Dirigidas. |
| **21** | Entrega da Segunda Lista de Exercícios (L2) e Resolução. |

---

## 📂 Estrutura do Repositório

O repositório está organizado de forma a separar os materiais de instrução, exercícios e gabaritos:

```
├── notebooks/                     # Diretório contendo os cadernos Jupyter das aulas
│   ├── Exercícios/                # Exercícios práticos contextualizados com cenários acústicos e navais
│   ├── Material/                  # PDFs com planejamento de aulas e apresentações teóricas
│   └── Professor/                 # Cadernos de apoio docente e gabaritos das atividades
├── data/                          # Diretório reservado para armazenamento de dados e leituras de arquivos
├── Dockerfile                     # Configurações do contêiner Docker para execução padronizada
├── Makefile                       # Atalhos para configuração do ambiente e execução do sistema
├── activate.sh                    # Script utilitário para gerenciamento do ambiente virtual Python
└── requirements.txt               # Relação de dependências e bibliotecas Python necessárias
```

---

## 🛠️ Instruções para Configuração do Ambiente

### Requisitos Prévios
*   Python 3.8 ou superior instalado localmente.
*   Ferramenta `make` (instalada nativamente em sistemas macOS/Linux).
*   Docker (opcional, recomendado para isolamento completo do ambiente).

### Opção 1: Configuração Local (Ambiente Virtual)

1.  **Instalação de Dependências**:
    Para criar automaticamente o ambiente virtual Python (`.rap-2026-env`) e instalar as dependências listadas em `requirements.txt`, execute o seguinte comando no terminal:
    ```bash
    make install
    ```

2.  **Inicialização do Jupyter Lab**:
    Após a instalação, ative o ambiente virtual e inicie a interface interativa do Jupyter Lab executando:
    ```bash
    make jupyter
    ```
    A interface do Jupyter será aberta no navegador padrão.

3.  **Limpeza de Caches e Arquivos Temporários**:
    Para limpar arquivos de cache do Python (`__pycache__`, `*.pyc`) e reiniciar o ambiente virtual:
    ```bash
    make clean
    ```

### Opção 2: Configuração via Docker (Recomendada para Padronização)

1.  **Construção da Imagem Docker**:
    Para construir a imagem Docker contendo o sistema e todas as dependências configuradas:
    ```bash
    make build
    ```

2.  **Execução do Contêiner**:
    Para inicializar o ambiente Jupyter Lab isolado dentro do contêiner:
    ```bash
    make run
    ```
    O servidor Jupyter estará disponível em seu navegador em `http://localhost:8888` (sem necessidade de senha). A pasta local `/data` será montada como volume compartilhado para persistência de dados.

---

## 📊 Metodologia de Avaliação

Conforme diretrizes do **Departamento de Aperfeiçoamento Avançado para Oficiais**, a avaliação de rendimento acadêmico constará de três etapas distintas e independentes:

1.  **Prova Escrita Individual (PI)**: Avaliação sem consulta de caráter presencial (pontuação de 0 a 100).
2.  **Lista Prática de Exercícios 1 (L1)**: Resolução individual de cenários computacionais (pontuação de 0 a 100).
3.  **Lista Prática de Exercícios 2 (L2)**: Resolução individual de análise de dados aplicada (pontuação de 0 a 100).

A Média Final ($MF$) do discente é obtida por meio da média aritmética simples:

$$MF = \frac{PI + L1 + L2}{3}$$

*   **Critério de Aprovação**: O discente estará aprovado na disciplina caso obtenha $MF \geq 70,0$. Caso contrário, será considerado reprovado.
*   **Formato de Entrega**: Todos os trabalhos práticos (listas de exercícios) deverão ser obrigatoriamente desenvolvidos e entregues no formato Jupyter Notebook (`.ipynb`), seguindo rigorosamente os modelos e diretrizes de formatação estabelecidos pelo corpo docente.

---

<div align="center">
  <i>Ministério da Defesa — Marinha do Brasil</i><br>
  <i>Centro de Instrução Almirante Alexandrino (CIAA)</i><br>
  <i>Especialização Avançada em Guerra Acústica — Turma 2026</i>
</div>
