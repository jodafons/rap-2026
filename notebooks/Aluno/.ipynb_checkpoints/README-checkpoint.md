# 📝 Área do Aluno (Espaço de Trabalho Individual)

Este diretório é o seu espaço de trabalho pessoal e exclusivo. Utilize esta pasta para criar seus cadernos de rascunho, resolver exercícios, fazer anotações e testar códigos em Python.

---

## 🔒 Segurança da Pasta

*   **Não Sincronizada**: Esta pasta está configurada no arquivo `.gitignore` do projeto. Isso significa que tudo o que você criar ou modificar aqui **não será enviado para o repositório central** e nem compartilhado com outros usuários.
*   **Imune a Atualizações**: O comando de atualização (`make update`) **ignora completamente esta pasta**. Seus arquivos aqui estão seguros e nunca serão deletados ou sobrescritos.

---

## ⚠️ AVISO IMPORTANTE: Perigos ao Trabalhar fora desta Pasta

> [!CAUTION]
> **Risco de Perda Permanente de Dados**
>
> Se você criar arquivos ou fizer alterações em arquivos **fora deste diretório `notebooks/Aluno/`** (como por exemplo editar diretamente cadernos de aulas nas outras pastas do repositório), essas alterações **serão excluídas permanentemente** ao executar o comando:
>
> ```bash
> make update
> ```

### Por que isso acontece?
O comando `make update` foi projetado para sincronizar de forma obrigatória todo o material do curso com a versão oficial mais recente. Para evitar conflitos de versão na máquina do aluno, ele realiza as seguintes ações:
1. Faz um descarte forçado (`git reset --hard`) de quaisquer modificações locais em arquivos oficiais.
2. Remove qualquer arquivo extra ou pasta que não faça parte do repositório oficial (`git clean -fd`), **com exceção apenas de `notebooks/Aluno/`**.

### Regra de Ouro:
*   **Quer salvar seu progresso/anotações?** Trabalhe **sempre** dentro de `notebooks/Aluno/`.
*   **Quer ver um caderno de aula?** Copie o arquivo da pasta oficial para a pasta `notebooks/Aluno/` e faça as suas modificações na sua cópia.
