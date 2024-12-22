def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as f:
        while True:
            new_line_input = input("Enter new line of content: ")
            if new_line_input == "stop":
                break
            else:
                f.write(new_line_input + "\n")


if __name__ == "__main__":
    main()
