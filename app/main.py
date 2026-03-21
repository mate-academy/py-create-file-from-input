def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    new_line = input("Enter new line of content: ")

    with open(file_name, "a") as f:
        while new_line != "stop":
            f.write(new_line + "\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
