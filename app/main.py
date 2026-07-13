def main() -> None:
    text = []
    name = input("Enter name of the file: ")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(line + "\n")
    with open(name + ".txt", "w") as text_file:
        text_file.writelines(text)


if __name__ == "__main__":
    main()
