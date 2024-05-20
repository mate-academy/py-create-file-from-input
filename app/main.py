def main() -> None:
    text = ""
    filename = input("Enter name of the file: ") + ".txt"
    while True:
        row = input("Enter new line of content: ")
        if row == "stop":
            break
        text += row + "\n"
    with open(filename, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
