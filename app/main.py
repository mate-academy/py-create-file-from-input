def main() -> None:
    lines_list = []

    file_name = input("Enter name of the file: ") + ".txt"

    while True:
        line_content = input("Enter new line of content: ")

        if line_content.strip().lower() == "stop":
            break

        lines_list.append(line_content + "\n")

    with open(file_name, "w") as file:
        file.writelines(lines_list)


if __name__ == "__main__":
    main()
