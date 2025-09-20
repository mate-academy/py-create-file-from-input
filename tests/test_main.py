import sys
import os

# Додаємо корінь проєкту у sys.path, щоб Python бачив пакет 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import main

def test_import():
    # Перевіряємо, що функція main імпортується і викликається
    assert callable(main)
