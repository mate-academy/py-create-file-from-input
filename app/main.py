def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"

    with open(name, "w") as file:
        while True:
            content = input("Enter new line of content: ")
            if content.lower() == "stop":
                break
            file.write(content + "\n")


if __name__ == "__main__":
    main()
