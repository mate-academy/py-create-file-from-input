def main() -> None:

    file_name = input("Enter name of the file: ") + ".txt"

    while True:
        message = input("Enter new line of content: ")
        with open(file_name, "a") as file:
            if message == "stop":
                break
            file.write(f"{message}\n")


if __name__ == "__main__":
    main()
