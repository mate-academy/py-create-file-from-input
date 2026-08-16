def main() -> None:
    file_name = input("Enter name of the file: ")
    lines_list = []
    if file_name:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            lines_list.append(line)
    with open(file_name + ".txt", "w") as file:
        file.write("\n".join(lines_list))


if __name__ == "__main__":
    main()
