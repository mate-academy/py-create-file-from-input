def main() -> None:
    file_name = input("Enter name of the file: ")
    file_n = open(file_name + ".txt", "a")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            content.append(line + "\n")
    file_n.writelines(content)
    file_n.close()


if __name__ == "__main__":
    main()
