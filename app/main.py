def main() -> None:
    name_file = input("Enter name of the file: ")
    new_line = input("Enter new line of content: ")
    with open(f"{name_file}.txt", "a") as f:
        while new_line != "stop":
            f.write(new_line + "\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
