def main() -> None:
    file_name = input("Enter name of the file: ")
    files_content = []
    new_line = ""

    while new_line != "stop":
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            files_content.append(f"{new_line}\n")

    with open(f"{file_name}.txt", "w") as file:
        for line in files_content:
            file.write(line)



if __name__ == "__main__":
    main()
