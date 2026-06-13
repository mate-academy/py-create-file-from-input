def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        file_content.append(line)

    with open(file_name + ".txt", "w") as file:
        for line in file_content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()

