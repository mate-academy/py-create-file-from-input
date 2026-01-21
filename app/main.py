def main() -> None:
    file_name: str = input("Enter name of the file: ")

    content: list[str] = []

    while True:
        line: str = input("Enter new line of content: ")

        if line == "stop":
            break

        content.append(line)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
