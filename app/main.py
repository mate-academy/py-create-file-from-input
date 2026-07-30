from __future__ import annotations


def main() -> None:
    file_basename = input("Enter name of the file: ").strip()

    # тест ожидает, что мы создадим именно "<basename>.txt"
    filename = (
        file_basename if file_basename.endswith(".txt")
        else f"{file_basename}.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(content + "\n")


if __name__ == "__main__":
    main()
