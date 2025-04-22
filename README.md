# My Machine Learning Project Template

This template is designed to serve as a flexible and maintainable starting point for machine learning projects. It provides an organized structure with configurations, secrets management and utilities for easy scaling and experimentation.

## Features

- **Modular Config Management**: YAML-based configuration files for different environments (local, production, testing, Kaggle).
- **Secret Management**: Built-in secret management with support for local and cloud environments.
- **Seamless Notebook Integration**: Jupyter notebooks pre-configured for quick experimentation.
- **Best Practices**: Structured project layout based on best practices for scalable and maintainable ML code.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Secrets Management](#secrets-management)
- [Data](#data)
- [Notebooks](#notebooks)
- [Development Setup](#development-setup)
- [Usage](#usage)
- [License](#license)

---

## Getting Started

To get started with this template, simply download or clone the repository and follow the steps below to set up your project.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ml-project-template.git
    ```

2. **Install dependencies**:    
    ```bash
    pip install -r requirements.txt
    ```

3. **Install the project in editable mode**:
    This will allow you to edit the code and have the changes reflected immediately without needing to reinstall the package:
    ```bash
    pip install -e .
    ```

---

## Project Structure

Here is an overview of the project structure:

```
ml-project-template/
├── configs/                       # Configuration files and secrets management
│   ├── config.kaggle.yaml          # Kaggle-specific configuration
│   ├── config_loader.py            # Main config loading logic
│   ├── config.local.yaml           # Local development configuration
│   ├── config.prod.yaml            # Production environment configuration
│   ├── config.test.yaml            # Test environment configuration
│   ├── __init__.py                 # Marks the directory as a Python package
│   └── secrets/                    # Secrets management (local/cloud)
│       ├── __init__.py             # Marks the secrets directory as a Python package
│       ├── kagglesecretmanager.py  # Kaggle secret manager
│       ├── localsecretmanager.py   # Local secret manager
│       ├── secretmanagerbase.py    # Base secret manager class
│       └── secretmanagerfactory.py # Factory to get secret manager instance
├── data/                           # Data storage
│   ├── processed/                  # Processed data
│   └── raw/                        # Raw data
├── kaggle_kernel_push.sh           # Script for pushing to Kaggle kernel
├── models/                         # Folder for saving models
├── notebooks/                      # Jupyter notebooks for experimentation
│   ├── 01_data_exploration.ipynb   # Data exploration notebook
│   ├── 02_training.ipynb           # Model training notebook
│   └── 03_inference.ipynb         # Model inference notebook
├── outputs/                        # Output files such as logs, metrics
│   └── logs/                       # Logs from the experiment
├── pyproject.toml                  # Project metadata and dependencies
├── README.md                       # Project description (this file)
├── requirements.txt                # Python dependencies
├── setup.py                        # Setup configuration for packaging
├── src/                            # Source code for the ML pipeline
│   ├── dataloader.py               # Data loading logic
│   ├── __init__.py                 # Marks the src directory as a Python package
│   ├── model.py                    # ML model definition
│   └── train.py                    # Model training logic
└── tests/                          # Unit tests
    └── test_config_loader.py       # Test case for config loader
```

### Key Folders:

- `configs/`: Contains all configuration files and secret management logic.
  - **config files** (`config.local.yaml`, `config.prod.yaml`, `config.test.yaml`, etc.) define environment-specific settings for the project.
  - **secrets** folder contains classes for managing secrets in different environments (`KaggleSecretManager`, `LocalSecretManager`).

- `data/`: Stores raw and processed data. Use this folder to keep your data organized.
  
- `models/`: Used for storing trained models.
  
- `notebooks/`: Contains Jupyter notebooks for experimenting with your data and models. It includes template notebooks for data exploration, training, and inference.

- `outputs/`: Logs and other output files related to model training, evaluation, etc.

- `src/`: Source code for the ML pipeline. This includes data loading, model training, and other essential utilities.
  
- `tests/`: Unit tests for verifying the functionality of core modules.

---

## Configuration

### How Configuration Works

The project uses environment-based configuration files, allowing for easy switching between different environments (e.g., local, production, testing, Kaggle). The environment is determined by the `ENV_NAME` variable in the `.env` file located in the project root.

Example `.env` file:
```env
ENV_NAME=local
```

The config files are:

- `config.local.yaml`: Configuration for local development.
- `config.prod.yaml`: Configuration for production.
- `config.test.yaml`: Configuration for testing.
- `config.kaggle.yaml`: Configuration for Kaggle kernels.

### Loading Configurations

You can load the configuration and secrets in your code using the `load_config()` function from the `config_loader.py` file:

```python
from configs.config_loader import load_config

config = load_config()

configs = config["configurations"]
directories = config["directories"]
secrets = config["secrets"]

print(configs)
print(directories)
print(secrets)
```

---

## Secrets Management

The `configs/secrets/` folder contains classes for managing secrets, which are environment-specific. The available secret managers are:

- **LocalSecretManager**: Manages local secrets from a YAML file.
- **KaggleSecretManager**: Manages secrets from Kaggle’s secret management system.

The `load_config()` function will automatically load the appropriate secret manager based on the environment.

---

## Data

The `data/` folder is used to store raw and processed data. Keep raw data under `data/raw/` and processed data under `data/processed/`.

---

## Notebooks

Jupyter notebooks are stored in the `notebooks/` folder. You can use these notebooks for data exploration, model training, and inference. The folder includes:

- **01_data_exploration.ipynb**: A notebook to explore and understand the dataset.
- **02_training.ipynb**: A notebook for model training.
- **03_inference.ipynb**: A notebook for running inference on the trained model.


This template is designed to be scalable and modular, making it easy to build upon for your machine learning projects.