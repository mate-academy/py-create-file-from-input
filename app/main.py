def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as f:
        new_line = ""
        while new_line != "stop":
            new_line = input("Enter new line of content: ")
            if new_line != "stop":
                f.write(new_line + "\n")


if __name__ == "__main__":
    main()
