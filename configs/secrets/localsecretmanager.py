import yaml
from pathlib import Path
from typing import List, Dict
from .secretmanagerbase import SecretManager

class LocalSecretManager(SecretManager):
    def __init__(self):
        super().__init__()
        self.secret_file = Path(__file__).resolve().parent / ".secrets.local.yaml"

    def get_secrets(self, keys: List[str]) -> Dict[str, str]:
        # If secrets file doesn't exist, log and return empty dict
        if not self.secret_file.exists():
            print(f"Secrets file not found at '{self.secret_file}'. Skipping secret loading.")
            return {}

        # Load secrets from the file
        with self.secret_file.open("r") as file:
            loaded_secrets = yaml.safe_load(file) or {}

        # Extract only the keys that exist in the loaded secrets
        found_secrets = {key: loaded_secrets[key] for key in keys if key in loaded_secrets}

        # Log any keys that were expected but not found
        missing_keys = [key for key in keys if key not in loaded_secrets]
        if missing_keys:
            print(f"[WARNING] The following secret keys were not found in '{self.secret_file}': {missing_keys}")

        return found_secrets



