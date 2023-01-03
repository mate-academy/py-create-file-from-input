def main() -> None:
    name = input("Enter name of the file: ")
    name1 = name + ".txt"
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(name1, "a") as file:
        for line in content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
