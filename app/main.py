def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        input_data = input("Enter new line of content: ")
        while input_data != "stop":
            file.write(input_data + "\n")
            input_data = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
