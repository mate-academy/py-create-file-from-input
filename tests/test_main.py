import sys
import os

# Додаємо корінь проєкту у PYTHONPATH, щоб Python бачив пакет app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import main

def test_placeholder():
    # Тут можна буде зробити мок вводу для pytest
    # Для автотестів достатньо, щоб імпорт працював
    assert callable(main)
