def main() -> None:
    name = input("Enter name of the file: ")

    if not name.endswith(".txt"):
        name += ".txt"

    with open(name, "w") as file:
        while True:
            content = input("Enter new line of content: ")

            if content == "stop":
                break

            file.write(content + "\n")


if __name__ == "__main__":
    main()
