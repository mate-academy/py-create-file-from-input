def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as user_file:
        line_input = input("Enter new line of content: ")
        while line_input != "stop":
            user_file.write(line_input + "\n")
            line_input = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
