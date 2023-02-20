def main() -> None:
    name_file = input("Enter name of the file: ")
    command = input("Enter new line of content: ")
    content = []
    while command != "stop":
        content.append(command)
        command = input("Enter new line of content: ")
    with open(f"{name_file}.txt", "a") as file:
        for line in content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
