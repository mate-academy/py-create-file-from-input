def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        input_line = input("Enter new line of content: ")
        if input_line == "stop":
            break
        lines.append(input_line)
    with open(file_name + ".txt", "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
