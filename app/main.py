def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ")
    file_lines = []
    while True:
        file_line = input("Enter new line of content: ")
        if file_line == "stop":
            break
        file_lines.append(file_line)
    with open(f"{file_name}.txt", "w") as file:
        for line in file_lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
