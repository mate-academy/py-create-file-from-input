def main() -> None:
    file_name: str = input("Enter name of the file: ")
    content: list[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    file_path: str = f"{file_name}.txt"
    with open(file_path, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
