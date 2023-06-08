def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    file_content = "\n".join(content)
    with open(file_name, "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
