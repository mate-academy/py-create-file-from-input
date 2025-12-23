def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            input_message = input("Enter new line of content: ")
            if input_message == "stop":
                break
            file.write(input_message + "\n")


if __name__ == "__main__":
    main()
