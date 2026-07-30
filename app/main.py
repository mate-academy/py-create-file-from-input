def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        while True:
            message = input("Enter new line of content: ")
            if message == "stop":
                break
            file.write(message + "\n")


if __name__ == "__main__":
    main()
