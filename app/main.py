def main() -> None:
    row = ""
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as new_file:
        while row != "stop":
            row = input("Enter new line of content: ")
            if row != "stop":
                new_file.write(row + "\n")


if __name__ == "__main__":
    main()
