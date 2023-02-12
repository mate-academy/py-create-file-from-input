def main() -> str:
    name_file = input("Enter name of the file: ")
    cycle = True
    content = ""
    while cycle:
        text = input("Enter new line of content: ")
        if text == "stop":
            cycle = False
        else:
            content += text + "\n"

    file_name = open(name_file + ".txt", "w")
    file_name.write(content)
    file_name.close()
    return file_name


if __name__ == "__main__":
    main()
