def main() -> None:
    name_of_the_file = input("Enter name of the file: ") + ".txt"

    new_line_of_content = input("Enter new line of content: ")

    content_to_write = []

    while new_line_of_content != "stop":

        if new_line_of_content != "stop":
            content_to_write.append(f"{new_line_of_content}\n")

        new_line_of_content = input("Enter new line of content: ")

    with open(name_of_the_file, "a") as file:
        for line in content_to_write:
            file.write(line)


if __name__ == "__main__":
    main()
