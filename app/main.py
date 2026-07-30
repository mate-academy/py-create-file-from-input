def main() -> None:
    name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)
    file_content = "\n".join(content)
    with open(f"{name}.txt", "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
