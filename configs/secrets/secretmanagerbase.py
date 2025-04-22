from abc import ABC, abstractmethod
from typing import List, Dict

class SecretManager(ABC):
    @abstractmethod
    def get_secrets(self, keys: List[str]) -> Dict[str, str]:
        pass

