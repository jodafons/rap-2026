<div align="center">
  <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8-blue.svg?style=flat-square" alt="Python Version"/>
  <img src="https://img.shields.io/badge/license-GPL--3.0-green.svg?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/framework-PyTorch_Lightning-orange.svg?style=flat-square" alt="PyTorch Lightning"/>
  <img src="https://img.shields.io/badge/dashboard-Dash-blue.svg?style=flat-square" alt="Dash"/>
  <img src="https://img.shields.io/badge/database-Cognite_SDK-yellow.svg?style=flat-square" alt="Cognite"/>
</div>

# 🎓 EEL-710-2026-01 (ITM Package)

Welcome to the **EEL-710-2026-01** repository! This project serves as a comprehensive toolkit and workspace for the course module, designed to seamlessly interface intelligent data engineering, scientific analysis, and interactive dashboarding using Python.

---

## 🎯 Purpose of the Repository

This repository provides an integrated suite of algorithms, components, and workflows built around the core `itm` package. Its primary objective is to allow students and developers to effectively perform machine learning, statistical modeling, and real-time data exploration.

**Key capabilities include:**
- 🔗 **Data Engineering**: Integration with the **Cognite SDK** for retrieving, processing, and navigating industrial Time Series and operational data.
- 🧠 **Machine Learning**: Utilization of **PyTorch Lightning** and **Scikit-Learn** for building robust, scalable predictive models.
- 📊 **Interactive Applications**: Creation of comprehensive visual interfaces and dashboards utilizing **Dash**, allowing for real-time model evaluation and data inspection.
- 🧪 **Experiment Tracking**: Systematic lifecycle management of ML experiments.

---

## 🚀 Getting Started with the Makefile

This repository leverages a `Makefile` to simplify environmental setup, dependency management, and running applications. It automatically uses an environment script (`activate.sh`) to gracefully configure the `.itm-env` virtual environment and necessary variables.

Here are the commands you can use from your terminal:

| Command | Description |
| :--- | :--- |
| `make install` or `make build` | 🏗️ **Configures the virtual environment & installs dependencies**<br>Executes `activate.sh`, builds the `.itm-env` virtual environment directory if it doesn't exist, and installs the `itm` package alongside all dependencies (e.g., PyTorch, Dash, Cognite) via `pip`. |
| `make jupyter` | 📓 **Starts the Jupyter environment**<br>Boots up a local `jupyter lab` instance using the project’s customized virtual environment without requiring a token or password. You can start creating your own notebooks immediately! |
| `make clean` | 🧹 **Cleans the repository**<br>Removes Python cache directories (`__pycache__`), byte-compiled code (`*.pyc`), and any left-over egg-info/build caches to keep the workspace neat and prevent caching issues. |

### Example Setup:
```bash
# 1. First, build and install all the project resources
make install

# 2. Launch the interactive Jupyter Lab interface to begin exploring
make jupyter
```

---

## 📖 Examples and Notebooks

To help you get acquainted with the library components and integrations quickly, we have provided a dedicated directory for step-by-step Jupyter Notebooks.

👉 **All usage examples and tutorials are located in the [`notebooks/`](./notebooks) folder.**

Start by exploring how to fetch operational data by following along with our entry-level guide:
* [`notebooks/How_to_connect_to_cognite.ipynb`](./notebooks/How_to_connect_to_cognite.ipynb)

Go ahead and experiment with new ideas in your own notebooks inside this directory. Happy coding!

---
<div align="center">
  <i>Maintained and developed for the EEL-710 2026.01 cohort.</i>
</div>
