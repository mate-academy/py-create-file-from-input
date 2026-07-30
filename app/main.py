def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    content = []
    new_line = input("Enter new line of content: ")

    while new_line != "stop":
        content.append(new_line)
        new_line = input("Enter new line of content: ")

    with open(filename, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
