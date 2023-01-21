def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(f"{file_name}", "a") as file:
        condition = True
        while condition:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                condition = False
            else:
                file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
