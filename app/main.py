from typing import List


def main() -> None:
    file_name: str = input("Enter name of the file: ").strip()
    lines: List[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    full_file_name: str = f"{file_name}.txt"

    with open(full_file_name, "w", encoding="utf-8") as file:
        for content_line in lines:
            file.write(content_line + "\n")


if __name__ == "__main__":
    main()
