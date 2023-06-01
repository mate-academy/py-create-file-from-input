def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "a") as file:
        while True:
            text = input("Enter new line of content: ")
            if text != "stop":
                file.write(text + "\n")
            else:
                break


if __name__ == "__main__":
    main()
