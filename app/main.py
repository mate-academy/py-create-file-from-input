def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = open(file_name, "w")

    while True:
        line_of_content = input("Enter new line of content: ")

        if line_of_content == "stop":
            break

        content.write(line_of_content + "\n")

    content.close()


if __name__ == "__main__":
    main()
