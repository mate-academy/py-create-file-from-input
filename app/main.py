def main() -> None:
    file_name = input("Enter name of the file: ")

    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    file_path = file_name + ".txt"
    with open(file_path, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
