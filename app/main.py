def main() -> None:
    name = input("Enter name of the file: ")
    content = []
    while True:
        string = input("Enter new line of content: ")
        if string == "stop":
            break
        content.append(string)
    with open(name + ".txt", "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
