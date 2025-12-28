def create_file_from_input() -> None:
    file_name = input("Enter name of the file: ").strip()
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    full_file_name = f"{file_name}.txt"

    with open(full_file_name, "w", encoding="utf-8") as f:
        for line in content_lines:
            f.write(line + "\n")

    print(
        f"File '{full_file_name}' created successfully with "
        f"{len(content_lines)} lines."
    )


def main() -> None:
    create_file_from_input()
