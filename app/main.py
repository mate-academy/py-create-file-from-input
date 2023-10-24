def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    input_text = input("Enter new line of content: ")
    with open(file_name, "w") as file:
        while input_text != "stop":
            file.write(input_text + "\n")
            input_text = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
