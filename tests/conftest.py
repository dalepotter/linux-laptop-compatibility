import pytest
from pathlib import Path

@pytest.fixture
def temp_output_dir(tmp_path):
    """Provide a temporary output directory for tests"""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir

@pytest.fixture
def sample_laptop_data():
    """Provide sample laptop data for testing"""
    return {
        'id': 'test-laptop-2020',
        'model': 'Test Laptop',
        'year': '2020',
        'manufacturer': 'Test',
        'processor': 'Intel Core i5',
        'confidence': 'High',
        'wifi_status': 'Works',
    }
