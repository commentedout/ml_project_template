import pytest
from configs.config_loader import load_config

def test_load_config_returns_expected_keys():
    config = load_config()
    assert "env_name" in config
    assert "configurations" in config
    assert "directories" in config
    assert "secrets" in config

