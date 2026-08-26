def main() -> None:
    file_input = input("Enter name of the file: ")
    with open(f"{file_input}.txt", "w") as file:
        current_input = ""
        while current_input != "stop":
            current_input = input("Enter new line of content: ")
            if current_input != "stop":
                file.write(f"{current_input}\n")


if __name__ == "__main__":
    main()
