def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"

    lines = []
    line = ""

    while line != "stop":
        line = input("Enter new line of content: ")

        if line != "stop":
            lines.append(line)

    with open(file_name, "w") as file:
        for one_line in lines:
            file.write(one_line + "\n")


if __name__ == "__main__":
    main()
