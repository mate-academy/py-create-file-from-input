def main() -> None:
    result = []
    name = input("Enter name of the file: ")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        result.append(new_line)
    name += ".txt"
    with open(name, "w") as file:
        for el in result:
            file.write(el + "\n")


if __name__ == "__main__":
    main()
