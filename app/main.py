def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        lines.append(content)

    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
