def main() -> None:
    text = ""
    name = ""
    name = input("Enter name of the file: ")
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            text += line + "\n"
        else:
            break
    with open(name + ".txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
