def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"
    input_file = open(name, "a")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        else:
            input_file.write(content + "\n")
    input_file.close()


if __name__ == "__main__":
    main()
