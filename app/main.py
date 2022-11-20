def main() -> None:
    name = input("Enter name of the file: ")

    with open(name + ".txt", "a") as file:

        while True:
            content = input("Enter new line of content: ")

            if content == "stop":
                break
            file.write(content + "\n")


if __name__ == "__main__":
    main()
