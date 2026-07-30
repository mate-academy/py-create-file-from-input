def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
