def main() -> None:
    file_name = input("Enter name of the file: ")
    add_lines = []
    while True:
        new_line = input("Enter new line of content: ")

        if new_line == "stop":
            break

        add_lines.append(new_line + "\n")

    with open(file_name + ".txt", "w") as file:
        file.writelines(add_lines)


if __name__ == "__main__":
    main()
