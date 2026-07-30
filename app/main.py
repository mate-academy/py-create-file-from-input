def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as file:
        message = input("Enter new line of content: ")
        while message != "stop":
            file.write(message + "\n")
            message = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
