def main() -> None:
    name_file = input("Enter name of the file: ")
    line = " "
    content = []
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            content.append(line)
    with open(f"{name_file}.txt", "w") as my_file:
        for text_line in content:
            my_file.write(text_line)
            my_file.write("\n")


if __name__ == "__main__":
    main()
