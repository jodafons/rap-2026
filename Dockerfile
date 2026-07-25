# Use official Ubuntu base image
FROM ubuntu:22.04

# Avoid prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

# Install Python, pip, and other necessary utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    git \
    bash-completion \
    wget \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory in the container
WORKDIR /app

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Install python requirements
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt


RUN mkdir -p notebooks/lessons

# Copy notebooks into the container
COPY notebooks/*.ipynb ./notebooks
COPY notebooks/lessons/* ./notebooks/lessons

# Create the data directory (to be used as a volume mount point)
RUN mkdir -p /app/data

# Copy custom bashrc for interactive shells system-wide
COPY .docker_bashrc /etc/bash.bashrc

# Expose default Jupyter Lab port
EXPOSE 8888

# Set default command to run Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--IdentityProvider.token=", "--ServerApp.password="]

