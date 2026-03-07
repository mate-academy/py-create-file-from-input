def main() -> None:
    name_app = input("Enter name of the file: ")
    full_name_app = name_app + ".txt"
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break

        content.append(line)

    with open(full_name_app, "a") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
