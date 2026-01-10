def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            message = input("Enter new line of content: ")
            if message.lower() == "stop":
                break
            file.write(f"{message}\n")


if __name__ == "__main__":
    main()
