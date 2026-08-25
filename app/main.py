def main() -> None:

    file_name = input("Enter name of the file: ")

    content = []

    while True:
        line_content = input("Enter new line of content: ")

        if line_content == "stop":
            break

        content.append(line_content)

    data = open(f"{file_name}.txt", "w")

    for line in content:
        data.write(f"{line}\n")

    data.close()


if __name__ == "__main__":
    main()
