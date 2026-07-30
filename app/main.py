def main() -> None:
    file_name = input("Enter name of the file: ")
    input_continue = True
    file_output = open(f"{file_name}.txt", "a")
    while input_continue:
        file_line = input("Enter new line of content: ")
        if file_line != "stop":
            file_output.write(f"{file_line}\n")
        if file_line == "stop":
            input_continue = False


if __name__ == "__main__":
    main()
