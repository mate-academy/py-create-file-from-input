def main() -> None:
    content = []
    file_names = input("Enter name of the file: ")
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)
    full_file_name = file_names + ".txt"

    with open(full_file_name, "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
