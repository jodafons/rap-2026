# Imagem base com Ubuntu e TeX Live completo para compilação do Planejamento RAP
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

# Instala TeX Live, pacotes necessários e utilitários
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-science \
    texlive-pstricks \
    texlive-pictures \
    texlive-lang-portuguese \
    texlive-extra-utils \
    latexmk \
    make \
    bash \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Comando padrão compila o planejamento
CMD ["make", "all"]
