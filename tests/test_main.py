import os
import pytest
from pytest import MonkeyPatch
from app.main import main


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self.filename):
            os.remove(self.filename)


@pytest.mark.parametrize(
    "file_basename,content",
    [
        (
            "name1",
            ["This is the first line of content", "This is the second"]
        ),
        (
            "hello_world",
            ["Python is great!", "FastApi is becoming popular", "What will be with Django in the future?"]
        ),
        (
            "i_am_empty",
            []
        ),
    ]
)
def test_main(file_basename: str, content: list, monkeypatch: MonkeyPatch):
    inputs = [file_basename, *content, "stop"]  # Включаємо "stop" для завершення введення
    input_messages = []

    def mock_input(text: str):
        input_messages.append(text)
        return inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    correct_filename = f"{file_basename}.txt"

    with CleanUpFile(correct_filename):
        main()

        assert input_messages == ["Enter name of the file: "] + ["Enter new line of content: "] * (len(content) + 1)

        assert os.path.exists(correct_filename)

        with open(correct_filename, "r") as f:
            assert f.read().splitlines() == content
