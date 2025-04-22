from pathlib import Path
from .secretmanagerbase import SecretManager

def get_secret_manager(env: str) -> SecretManager:
    if env == "local":
        from .localsecretmanager import LocalSecretManager            
        return LocalSecretManager()
    elif env == "kaggle":
        from .kagglesecretmanager import KaggleSecretManager
        return KaggleSecretManager()
    else:
        raise NotImplementedError(f"Secret manager not implemented for environment: {env}")
    
