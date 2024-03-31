def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            text.append(line)
        else:
            break

    f = open(filename, "w")
    for line in text:
        f.write(line + "\n")
    f.close()


if __name__ == "__main__":
    main()
