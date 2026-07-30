def main() -> str:
    new_file_name = input("Enter name of the file: ")
    content = []
    line = input("Enter new line of content: ")
    while line != "stop":
        content.append(line)
        line = input("Enter new line of content: ")
    new_file = open(new_file_name + ".txt", "w")
    for line in content:
        new_file.write(line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
