def main() -> None:
    create_file = input("Enter name of the file: ")
    file_content = []
    create_file_txt = create_file + ".txt"

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            file_content.append(line)

    with open(create_file_txt, "a") as f:
        for line in file_content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
