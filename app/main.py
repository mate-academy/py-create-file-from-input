def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            input_line = input("Enter new line of content: ")
            if input_line == "stop":
                break
            file.write(f"{input_line}\n")


if __name__ == "__main__":
    main()
