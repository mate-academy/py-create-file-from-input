def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    line = input("Enter new line of content: ")
    while line != "stop":
        file_content.append(f"{line}\n")
        line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as fin:
        for line in file_content:
            fin.write(line)


if __name__ == "__main__":
    main()
