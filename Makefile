SHELL := /bin/bash

# Docker parameters (can be overridden from the command line)
PORT ?= 8888
DATA_VOLUME ?= $(shell pwd)/data
IMAGE_NAME ?= rap-2026
IMAGE_TAG ?= latest
REGISTRY ?= jodafons

# Build full image tag dynamically depending on whether REGISTRY is set
ifeq ($(REGISTRY),)
    IMAGE_FULL_NAME := $(IMAGE_NAME):$(IMAGE_TAG)
else
    IMAGE_FULL_NAME := $(REGISTRY)/$(IMAGE_NAME):$(IMAGE_TAG)
endif

.PHONY: all build install jupyter clean push pull run update

all: build

# Instala as dependências e configura o ambiente
install: build

# Inicia o Jupyter Lab
jupyter:
	@echo "📓 Iniciando Jupyter Lab..."
	@source activate.sh && jupyter lab --IdentityProvider.token="" --ServerApp.password=""

# Limpa arquivos temporários e caches
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .rap-2026-env
	
# --- Docker Targets ---

# Build docker image
build:
	@echo "🐳 Building Docker image $(IMAGE_FULL_NAME)..."
	docker build -t $(IMAGE_FULL_NAME) .

# Push docker image to registry
push:
	@if [ -z "$(REGISTRY)" ]; then \
		echo "❌ Error: REGISTRY variable is not set. Cannot push. Try: make push REGISTRY=myregistry.com"; \
		exit 1; \
	fi
	@echo "🚀 Pushing Docker image $(IMAGE_FULL_NAME)..."
	docker push $(IMAGE_FULL_NAME)

# Pull docker image from registry
pull:
	@echo "📥 Pulling Docker image $(IMAGE_FULL_NAME)..."
	docker pull $(IMAGE_FULL_NAME)

# Run container with parameterized port and volume
run:
	@echo "🏃 Running Docker container..."
	@echo "🔗 Jupyter will be available at: http://localhost:$(PORT)"
	@echo "📂 Mount directory (local): $(DATA_VOLUME)"
	@mkdir -p $(DATA_VOLUME)
	docker run -it --rm \
		-p $(PORT):8888 \
		-v "$(DATA_VOLUME):/app/data" \
		$(IMAGE_FULL_NAME)

# Atualiza o repositório Git de acordo com o repositório central, preservando a pasta notebooks/Aluno/
update:
	@echo "🔍 Verificando repositório..."
	@git fetch --all
	@UPSTREAM=$$(git rev-parse --abbrev-ref @{u} 2>/dev/null || echo "origin/main"); \
	HAS_CHANGES=$$(git status --porcelain | grep -v '^??' || true); \
	if [ -n "$$HAS_CHANGES" ]; then \
		echo "📦 Alterações locais detectadas. Salvando backup temporário com git stash..."; \
		if git stash; then \
			echo "💾 Backup salvo."; \
		else \
			echo "❌ Falha ao criar backup. Abortando."; \
			exit 1; \
		fi; \
	fi; \
	echo "🔄 Forçando sincronização de todo o resto com o repositório central ($$UPSTREAM)..."; \
	git reset --hard $$UPSTREAM; \
	echo "🧹 Limpando arquivos extras (mantendo notebooks/Aluno)..."; \
	git clean -fd -e "notebooks/Aluno/"; \
	echo "✅ Repositório atualizado com sucesso de acordo com o repositório central!"