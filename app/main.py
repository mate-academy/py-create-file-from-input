def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "a") as file:
        new_line = input("Enter new line of content: ")
        while new_line != "stop":
            file.write(f"{new_line}\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
