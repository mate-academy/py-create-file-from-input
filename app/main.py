def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        data = input("Enter new line of content: ")
        if data.lower() == "stop":
            break
        content.append(data)

    with open(name, "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
