def main() -> None:
    is_true = True
    title = input("Enter name of the file: ")
    while is_true:
        with open(title + ".txt", "a") as file:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                is_true = False
            else:
                file.write(new_line + "\n")


if __name__ == "__main__":
    main()
