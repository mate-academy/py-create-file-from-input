def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "x") as file:
        while True:
            content_input = input("Enter new line of content: ")
            if content_input == "stop":
                break
            else:
                file.write(f"{content_input}\n")


if __name__ == "__main__":
    main()
