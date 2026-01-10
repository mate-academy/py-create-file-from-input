def main() -> None:
    line = ""
    file_content = []
    file_name = input("Enter name of the file: ")
    if file_name:
        while line != "stop":
            line = input("Enter new line of content: ")
            file_content.append(line + "\n")

    with open(file_name + ".txt", "w") as f:
        for line in file_content[:-1]:
            f.write(line)


if __name__ == "__main__":
    main()
