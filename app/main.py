def main() -> None:
    file_name = input("Enter name of the file: ")
    current_line = ""
    current_line_list = []
    while current_line != "stop":
        current_line = input("Enter new line of content: ")
        if current_line != "stop":
            current_line_list.append(f"{current_line}")
    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(current_line_list))


if __name__ == "__main__":
    main()
