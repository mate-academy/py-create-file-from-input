def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"
    with open(name, "a") as file:
        message = input("Enter new line of content: ")
        while message != "stop":
            file.write(message + "\n")
            message = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
