from __future__ import annotations


def create_text_file() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    full_filename = f"{file_name}.txt"

    with open(full_filename, "w", encoding="utf-8") as file:
        file.write("\n".join(content_lines))

    print(f"File successfully created: {full_filename}")


if __name__ == "__main__":
    create_text_file()

