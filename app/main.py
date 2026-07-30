def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as new_file:
        new_line = input("Enter new line of content: ")
        while new_line != "stop":
            new_file.write(new_line + "\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
