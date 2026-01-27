def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    input_line = input("Enter new line of content: ")
    with open(file_name, "w") as file:
        while input_line != "stop":
            file.write(input_line)
            file.write("\n")
            input_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
