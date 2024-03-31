def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            text.append(line)
        else:
            break

    new_file = open(filename, "w")
    for line in text:
        new_file.write(line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
