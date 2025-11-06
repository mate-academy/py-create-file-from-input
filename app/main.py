def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text = text + line + "\n"
    file_to_write = open(file_name + ".txt", "w")
    file_to_write.write(text)


if __name__ == "__main__":
    main()
