def main() -> None:
    content = []
    name = input("Enter name of the file: ")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        content.append(text)

    name_of_file = name + ".txt"
    with open(name_of_file, "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
