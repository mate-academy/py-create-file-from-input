def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    filen = open(filename, "w")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        filen.write(text + "\n")
    filen.close()
    pass


if __name__ == "__main__":
    main()
