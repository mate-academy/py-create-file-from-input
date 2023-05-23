def main() -> None:
    name = input("Enter name of the file: ")
    text = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text += line + "\n"

    opened_file = open(name + ".txt", "w")
    opened_file.write(text)
    opened_file.close()


if __name__ == "__main__":
    main()
