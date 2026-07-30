def main() -> None:
    file_name = input("Enter name of the file: ")
    working_with_file = True
    with open(f"{file_name}.txt", "w") as f:
        while working_with_file:
            input_data = input("Enter new line of content: ")
            if input_data.lower() == "stop":
                working_with_file = False
            else:
                f.write(f"{input_data}\n")


if __name__ == "__main__":
    main()
