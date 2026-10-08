SHELL := /bin/bash

# Configurações da Imagem Docker
IMAGE_NAME ?= rap-latex:latest

# Listas disponíveis
LISTAS_ALL := 1 2 3 4 5 6 7 8 9 10 11
LISTAS_TARGETS := 1 2 3 4 5 6 7 8 9 10 11 01 02 03 04 05 06 07 08 09

.PHONY: all all-listas $(LISTAS_TARGETS) compile_lista build-image shell clean clean-temp distclean help _docker_compile_lista

# Alvo padrão: compila todas as listas (01 a 11)
all: all-listas

# Compilar todas as listas (01 a 11)
all-listas:
	@echo "🐳 Iniciando compilação de todas as listas (01 a 11) via Docker..."
	@for n in $(LISTAS_ALL); do \
		$(MAKE) $$n; \
	done
	@echo "🎉 Todas as listas (01 a 11) foram compiladas com sucesso!"

# Regras dinâmicas para compilar lista individual por número: make 1 .. make 11
$(LISTAS_TARGETS):
	@$(MAKE) compile_lista NUM=$@

# Compilação via Docker de uma lista específica
compile_lista:
	@if [ -z "$(NUM)" ]; then \
		echo "❌ Especifique o número da lista. Ex: make 1, make 2, ..., make 9"; \
		exit 1; \
	fi; \
	NUM_FMT=$$(python3 -c "print(f'{int(\"$(NUM)\"):02d}')"); \
	if [ -z "$$(docker images -q $(IMAGE_NAME) 2> /dev/null)" ]; then \
		echo "🐳 Imagem $(IMAGE_NAME) não encontrada. Construindo imagem Docker..."; \
		docker build -t $(IMAGE_NAME) .; \
	fi; \
	echo "🐳 Compilando Lista $$NUM_FMT (Com e Sem Gabarito) no contêiner Docker..."; \
	docker run --rm -v "$$(pwd):/workspace" $(IMAGE_NAME) make _docker_compile_lista NUM=$$NUM_FMT; \
	$(MAKE) clean-temp; \
	echo "✅ Lista $$NUM_FMT compilada com sucesso e arquivos temporários limpos!"

# Construção da imagem Docker
build-image:
	@echo "🐳 Construindo imagem Docker '$(IMAGE_NAME)'..."
	docker build -t $(IMAGE_NAME) .

# Shell interativo no contêiner
shell:
	@echo "🐳 Abrindo terminal no contêiner Docker..."
	docker run -it --rm -v "$$(pwd):/workspace" $(IMAGE_NAME) /bin/bash

# ==============================================================================
# Alvo interno de compilação (executado apenas dentro do contêiner Docker)
# ==============================================================================
_docker_compile_lista:
	@NUM_FMT=$$(python3 -c "print(f'{int(\"$(NUM)\"):02d}')"); \
	PDF_GAB="Aula $$NUM_FMT - Lista de Exercícios (Gabarito).pdf"; \
	PDF_ALU="Aula $$NUM_FMT - Lista de Exercícios.pdf"; \
	echo "📄 [Docker] Compilando '$$PDF_GAB'..."; \
	pdflatex -shell-escape -interaction=nonstopmode -jobname="main_gabarito" "\def\numAula{$$NUM_FMT}\def\comGabarito{true}\input{main.tex}" > /dev/null; \
	pdflatex -shell-escape -interaction=nonstopmode -jobname="main_gabarito" "\def\numAula{$$NUM_FMT}\def\comGabarito{true}\input{main.tex}"; \
	cp main_gabarito.pdf "$$PDF_GAB"; \
	echo "✅ [Docker] Gerado: '$$PDF_GAB'"; \
	echo "📄 [Docker] Compilando '$$PDF_ALU'..."; \
	pdflatex -shell-escape -interaction=nonstopmode -jobname="main_aluno" "\def\numAula{$$NUM_FMT}\def\comGabarito{false}\input{main.tex}" > /dev/null; \
	pdflatex -shell-escape -interaction=nonstopmode -jobname="main_aluno" "\def\numAula{$$NUM_FMT}\def\comGabarito{false}\input{main.tex}"; \
	cp main_aluno.pdf "$$PDF_ALU"; \
	echo "✅ [Docker] Gerado: '$$PDF_ALU'"; \
	rm -rf _minted* *.aux *.log *.out *.toc *.nav *.snm *.vrb *.fls *.fdb_latexmk *.synctex.gz *.bbl *.blg *.dvi *.ps *.pyg main_gabarito* main_aluno* main.pdf *.w18

# ==============================================================================
# Limpeza de arquivos temporários e intermediários
# ==============================================================================
clean-temp:
	@rm -rf _minted* .auctex-auto auto
	@rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.fls *.fdb_latexmk *.synctex* *.bbl *.blg *.dvi *.ps *.pyg *.w18 *.bcf *.run.xml *.lot *.lof
	@rm -f "Aula "*.aux "Aula "*.log "Aula "*.out "Aula "*.pyg "Aula "*.toc "Aula "*.fls "Aula "*.fdb_latexmk "Aula "*.synctex*
	@rm -f main_gabarito* main_aluno* main.pdf test_*

# Limpeza padrão: remove todos os arquivos temporários (.out, .log, .aux, _minted, etc.) e PDFs gerados
clean: clean-temp
	@rm -f "Aula "*".pdf" *.pdf
	@echo "🧹 Todos os arquivos temporários (.out, .log, .aux, _minted, etc.) e PDFs foram removidos."

# Limpeza completa (alias para clean)
distclean: clean

help:
	@echo "=================================================================="
	@echo "  Makefile - Compilação de Listas de Exercícios (Docker)"
	@echo "=================================================================="
	@echo "  make all (ou make)       - Compila TODAS as listas (01 a 11)"
	@echo "  make 1                   - Compila Lista 01 (com e sem gabarito)"
	@echo "  make 2                   - Compila Lista 02 (com e sem gabarito)"
	@echo "  ..."
	@echo "  make 11                  - Compila Lista 11 (com e sem gabarito)"
	@echo "  make clean               - Remove arquivos temporários e PDFs gerados"
	@echo "  make distclean           - Remove arquivos temporários e PDFs gerados"
	@echo "  make build-image         - Reconstrói a imagem Docker"
	@echo "  make shell               - Abre terminal interativo no Docker"
	@echo "=================================================================="
