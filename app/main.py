def main() -> None:
    name = input("Enter name of the file: ")
    new_line = input("Enter new line of content: ")
    text = []
    while new_line != "stop":
        text.append(new_line)
        new_line = input("Enter new line of content: ")
    with open(name + ".txt", "a") as f:
        f.write("\n".join(text))


if __name__ == "__main__":
    main()
