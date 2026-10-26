SHELL := /bin/bash

# Configurações
DOC_NAME ?= Planejamento
IMAGE_NAME ?= rap-latex:latest

.PHONY: all compile-local build-image shell clean distclean help

# Alvo padrão: compila automaticamente via Docker
all:
	@if [ -z "$$(docker images -q $(IMAGE_NAME) 2> /dev/null)" ]; then \
		echo "🐳 Imagem $(IMAGE_NAME) não encontrada. Construindo imagem Docker..."; \
		docker build -t $(IMAGE_NAME) .; \
	fi
	@echo "🐳 Compilando $(DOC_NAME).tex usando contêiner Docker..."
	@docker run --rm -v "$$(pwd):/workspace" $(IMAGE_NAME) make compile-local DOC_NAME=$(DOC_NAME)

help:
	@echo "=================================================================="
	@echo "  Comandos para compilação do Planejamento (Padrão: Docker)"
	@echo "=================================================================="
	@echo "  make                     - Compila $(DOC_NAME).tex no Docker gerando $(DOC_NAME).pdf"
	@echo "  make compile-local       - Compila localmente sem Docker"
	@echo "  make build-image         - Reconstrói a imagem Docker"
	@echo "  make shell               - Abre terminal interativo no Docker"
	@echo "  make clean               - Remove arquivos temporários de compilação"
	@echo "  make distclean           - Remove temporários e o arquivo $(DOC_NAME).pdf"
	@echo "=================================================================="

# Compilação interna direta (executada dentro do contêiner ou localmente)
compile-local:
	@echo "📄 Executando pdflatex em main.tex..."
	pdflatex -shell-escape -interaction=nonstopmode -jobname="$(DOC_NAME)" main.tex
	pdflatex -shell-escape -interaction=nonstopmode -jobname="$(DOC_NAME)" main.tex
	@echo "✅ Gerado com sucesso: $(DOC_NAME).pdf"

# Construção explícita da imagem Docker
build-image:
	@echo "🐳 Construindo imagem Docker '$(IMAGE_NAME)'..."
	docker build -t $(IMAGE_NAME) .

# Shell interativo no contêiner
shell:
	@echo "🐳 Abrindo terminal no contêiner Docker..."
	docker run -it --rm -v "$$(pwd):/workspace" $(IMAGE_NAME) /bin/bash

# Limpeza de arquivos temporários do LaTeX
clean:
	@echo "🧹 Removendo arquivos temporários..."
	@rm -rf _minted* *.aux *.log *.out *.toc *.nav *.snm *.vrb *.fls *.fdb_latexmk *.synctex.gz *.bbl *.blg *.dvi *.ps

# Limpeza completa (inclui o PDF gerado)
distclean: clean
	@echo "🧹 Removendo $(DOC_NAME).pdf..."
	@rm -f $(DOC_NAME).pdf
