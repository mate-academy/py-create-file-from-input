def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(f"{name_of_file}.txt", "a") as saving_file:
        while True:
            new_line_input = input("Enter new line of content: ")
            if new_line_input != "stop":
                saving_file.write(f"{new_line_input}\n")
            else:
                break


if __name__ == "__main__":
    main()
