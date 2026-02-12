def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    new_line = input("Enter new line of content: ")
    lines_list = []
    while new_line != "stop":
        lines_list.append(new_line)
        new_line = input("Enter new line of content: ")

    with open(file_name, "w") as file:
        file.write("\n".join(lines_list))


if __name__ == "__main__":
    main()
