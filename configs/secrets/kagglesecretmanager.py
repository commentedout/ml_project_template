from kaggle_secrets import UserSecretsClient
from typing import List, Dict
from .secretmanagerbase import SecretManager

class KaggleSecretManager(SecretManager):
    def __init__(self):
        self.client = UserSecretsClient()

    def get_secrets(self, keys: List[str]) -> Dict[str, str]:
        return {key: self.client.get_secret(key) for key in keys}
    