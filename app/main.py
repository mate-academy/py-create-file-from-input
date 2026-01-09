def main() -> None:
    file_name = input("name of the file: ").strip()

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content: list[str] = []

    while True:
        line = input("new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
