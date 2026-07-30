def main() -> None:
    filename = input("Enter name of the file: ")
    new_file = open(filename + ".txt", "w+")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        new_file.write(content + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
