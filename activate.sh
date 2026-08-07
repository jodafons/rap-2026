#!/bin/bash

# Identifica o Sistema Operacional
OS="$(uname -s)"
case "$OS" in
    Darwin)
        OS_NAME="macOS"
        ;;
    Linux)
        OS_NAME="Linux"
        ;;
    *)
        OS_NAME="Desconhecido ($OS)"
        ;;
esac
echo "🖥️ Sistema Operacional: $OS_NAME"

# Verifica se o Git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Erro: Git não está instalado no sistema."
    return 1 2>/dev/null || exit 1
fi
echo "✅ Git detectado."

# Verifica e detecta a versão correta do Python (independente de python/python3)
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    if python -c "import sys; sys.exit(0 if sys.version_info.major == 3 else 1)" &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo "❌ Erro: Python 3 não foi encontrado. Este projeto requer Python 3."
        return 1 2>/dev/null || exit 1
    fi
else
    echo "❌ Erro: Python não está instalado no sistema."
    return 1 2>/dev/null || exit 1
fi
PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")')
echo "✅ Python 3 detectado ($PYTHON_CMD, versão $PYTHON_VERSION)."

# Verifica se o pip está instalado, se não tiver, instala via ensurepip
if ! $PYTHON_CMD -m pip --version &> /dev/null; then
    echo "📦 pip não encontrado. Tentando instalar via ensurepip..."
    if $PYTHON_CMD -m ensurepip --default-pip &> /dev/null; then
        echo "✅ pip instalado com sucesso."
    else
        echo "❌ Erro: Não foi possível instalar o pip. Por favor, instale o pip manualmente."
        return 1 2>/dev/null || exit 1
    fi
else
    echo "✅ pip detectado."
fi

# Verifica se o virtualenv está instalado, se não tiver, instala
USE_VENV=false
if ! command -v virtualenv &> /dev/null; then
    echo "📦 virtualenv não encontrado. Tentando instalar..."
    if $PYTHON_CMD -m pip install --upgrade pip &> /dev/null; then
        :
    fi
    if $PYTHON_CMD -m pip install virtualenv &> /dev/null || $PYTHON_CMD -m pip install --user virtualenv &> /dev/null; then
        echo "✅ virtualenv instalado com sucesso."
    else
        echo "⚠️ Não foi possível instalar o virtualenv usando pip. Usando módulo nativo 'venv' do Python."
        USE_VENV=true
    fi
else
    echo "✅ virtualenv detectado."
fi

# Define caminhos do ambiente virtual
export VIRTUALENV_NAMESPACE='.rap-2026-env'
export LOGURU_LEVEL="DEBUG"
export VIRTUALENV_PATH=$PWD/$VIRTUALENV_NAMESPACE

if [ -d "$VIRTUALENV_PATH" ]; then
    echo "✅ Ambiente virtual '$VIRTUALENV_NAMESPACE' encontrado. Ativando..."
    source "$VIRTUALENV_PATH/bin/activate"
else
    echo "🔨 Ambiente virtual não encontrado. Criando em '$VIRTUALENV_PATH'..."
    if [ "$USE_VENV" = "true" ]; then
        $PYTHON_CMD -m venv "$VIRTUALENV_PATH"
    else
        virtualenv -p "$PYTHON_CMD" "$VIRTUALENV_PATH"
    fi
    
    source "$VIRTUALENV_PATH/bin/activate"
    echo "📥 Instalando dependências listadas em requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi
