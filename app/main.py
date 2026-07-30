def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    write = " "
    file_content = []
    while write != "stop":
        new_line = input("Enter new line of content: ")
        file_content.append(new_line)
        write = new_line.lower()
    file_content.pop(len(file_content) - 1)
    with open(f"{file_name}", "w", encoding="utf8") as fichier:
        for line in file_content:
            fichier.write(line + "\n")


if __name__ == "__main__":
    main()
