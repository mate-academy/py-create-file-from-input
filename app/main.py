def main() -> None:
    filename = input("Enter name of the file: ")

    content = ""
    while (line := input("Enter new line of content: ")) != "stop":
        content += line + "\n"

    with open(filename + ".txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
