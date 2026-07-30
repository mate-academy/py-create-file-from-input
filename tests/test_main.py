import sys
import os
import pytest
from pytest import MonkeyPatch

# додаємо корінь проєкту у sys.path, щоб Python бачив пакет `app`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import main


class CleanupFile:
    def __init__(self, filename: str):
        self._filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self._filename):
            os.remove(self._filename)


@pytest.mark.parametrize(
    "file_basename,content",
    [
        ("name1", ["This is the first line of content", "This is the second"]),
        ("hello_world", ["Python is great!", "FastApi is becoming popular", "What will be with Django in the future?"]),
        ("i_am_empty", []),
    ],
)
def test_main(file_basename: str, content: list, monkeypatch: MonkeyPatch):
    inputs = [file_basename, *content, "stop"]
    input_messages = []

    def mock_input(text: str):
        input_messages.append(text)
        return inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    correct_filename = f"{file_basename}.txt"

    with CleanupFile(correct_filename):
        main()

        # перевіряємо що правильні запитання були задані
        assert input_messages == ["Enter name of the file: "] + ["Enter new line of content: "] * (len(content) + 1)

        # перевіряємо що файл створився
        assert os.path.exists(correct_filename)

        with open(correct_filename, "r", encoding="utf-8") as f:
            assert f.read().splitlines() == content


def test_import():
    # перевіряємо, що функція main імпортується і викликається
    assert callable(main)
