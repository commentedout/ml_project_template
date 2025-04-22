import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from configs.secrets.secretmanagerfactory import get_secret_manager


# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIGS_DIR = BASE_DIR / "configs"

def is_kaggle():
    return Path("/kaggle/input").exists()


def detect_env() -> str:
    #If running on Kaggle, return 'kaggle'. Do not load .env file.
    if is_kaggle():
        return "kaggle"
    
    ENV_FILE_PATH = BASE_DIR / ".env"
    if not ENV_FILE_PATH.exists():
        raise FileNotFoundError(f".env file not found at root.")

    load_dotenv(ENV_FILE_PATH)
    env_name = os.getenv("ENV_NAME")

    if not env_name:
        raise EnvironmentError("ENV_NAME not set in the .env file.")
    
    return env_name.strip()
    


def load_yaml_config(env_name: str) -> dict:
    config_path = CONFIGS_DIR / f"config.{env_name}.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"YAML config file not found for environment '{env_name}': {config_path}")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def fetch_secrets(env_name: str, secret_keys: dict) -> dict:    
    secret_manager = get_secret_manager(env_name)
    keys = secret_keys.get("keys", [])

    if not isinstance(keys, list):
        raise ValueError("Expected 'keys' under 'secrets' to be a list.")

    secrets = secret_manager.get_secrets(keys)
    return secrets


def load_config():
    env_name = detect_env()
    full_config = load_yaml_config(env_name)

    try:
        configurations = full_config["configurations"]
        directories = full_config["directories"]
        secret_keys = full_config.get("secrets", {})
    except KeyError as e:
        raise KeyError(f"Missing expected section in YAML: {e}")
    
    #fetch secrets as per environment
    secrets = fetch_secrets(env_name, secret_keys)

    return {
        "env_name": env_name,
        "configurations": configurations,
        "directories": directories,
        "secrets": secrets,
    }


# for local debugging
# if __name__ == "__main__":
#     config = load_config()
#     print("Environment:", config["env_name"])
#     print("Configurations:", config["configurations"])
#     print("Directories:", config["directories"])
#     print("Secrets:", config["secrets"])  
