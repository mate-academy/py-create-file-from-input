def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")  # Зміна тут
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, mode="w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f'# File name: "{file_name}"')
    print("# File content:")
    for line in content_lines:
        print(f"# {line}")


if __name__ == "__main__":
    main()
