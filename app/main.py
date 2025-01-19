def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as current_file:
        while True:
            current_line = input("Enter new line of content: ")
            if current_line == "stop":
                break
            current_file.write(f"{current_line}\n")


if __name__ == "__main__":
    main()
