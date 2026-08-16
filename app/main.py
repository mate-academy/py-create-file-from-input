def main() -> None:
    file_name = input("Enter name of the file: ")

    file_content = []

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        file_content.append(line)

    file_content = "\n".join(file_content)

    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
