import sys
import os
import pytest

from pytest import MonkeyPatch

# додаємо корінь проєкту у sys.path, щоб Python бачив пакет `app`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import main

