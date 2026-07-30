def main() -> None:
    filename = input("Enter name of the file: ")

    content = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content += line + "\n"

    with open(filename + ".txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
