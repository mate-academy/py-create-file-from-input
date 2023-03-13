def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "a") as file:
        while True:
            message = input("Enter new line of content: ")
            if message == "stop":
                break
            file.write(f"{message}\n")


if __name__ == "__main__":
    main()
