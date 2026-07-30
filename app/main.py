def main() -> None:
    file_name = input("Enter name of the file: ")

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(f"{file_name}.txt", "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
