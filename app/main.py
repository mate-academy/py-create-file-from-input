def main() -> None:
    name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    file_name = f"{name}.txt"

    with open(file_name, "w") as file:
        for line in content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
