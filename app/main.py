def main() -> None:
    name_of_file = input("Enter name of the file: ")
    content_of_file = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_of_file.append(line)

    with open(f"{name_of_file}.txt", "w") as file:
        for line in content_of_file:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
