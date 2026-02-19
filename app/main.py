def main() -> None:
    filename = input("Enter name of the file: ")
    text = []
    nextline = ""
    while nextline != "stop":
        nextline = input("Enter new line of content: ")
        if nextline != "stop":
            text.append(nextline)

    filename += ".txt"

    with open(filename, "w") as f:
        f.write("\n".join(text))


if __name__ == "__main__":
    main()
