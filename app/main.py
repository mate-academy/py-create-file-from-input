def main() -> str:
    name = input("Enter name of the file: ")
    name += ".txt"
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line + "\n")
    with open(name, "a") as file:
        file.writelines(content)


if __name__ == "__main__":
    main()
