def main() -> str:
    filename = input("Enter name of the file: ")
    file_content = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file_content.append(new_line)
    with open(filename + ".txt", "w") as f:
        for line in file_content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
