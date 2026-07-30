def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(f"{name_of_file}.txt", "a") as file:
        while name_of_file != "":
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
