from typing import List


def create_file() -> None:
    file_name = input("Enter name of the file: ")
    lines: List[str] = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    file_content = "\n".join(lines)
    file_name += ".txt"
    with open(file_name, "w") as file:
        file.write(file_content)
    print(f'# File name: "{file_name}"')
    print("# File content:")
    for line in lines:
        print("# " + line)


def main() -> None:
    create_file()


if __name__ == "__main__":
    main()
