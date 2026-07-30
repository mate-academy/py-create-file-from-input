def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"
    content = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content += line + "\n"

    with open(name_file, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
