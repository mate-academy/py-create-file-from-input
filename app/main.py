def main() -> None:
    text_file = ""
    text = input("Enter name of the file: ")
    new_file = open(text + ".txt", "w")
    while text_file != "stop":
        text_file = input("Enter new line of content: ")
        if text_file != "stop":
            new_file.write(text_file + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
