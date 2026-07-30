def main() -> None:
    name = input("Enter name of the file: ")

    with open(name + ".txt", "w") as file:
        pass

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        with open(name + ".txt", "a") as file:
            file.write(content + "\n")


if __name__ == "__main__":
    main()
