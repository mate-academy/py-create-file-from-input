def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "a") as file:
        input_value = None

        while input_value != "stop":
            input_value = input("Enter new line of content: ")
            if input_value != "stop":
                file.write(input_value + "\n")


if __name__ == "__main__":
    main()
