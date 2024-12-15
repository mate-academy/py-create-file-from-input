
def main() -> None:
    name = input("Enter name of the file: ")

    new_line = input("Enter new line of content: ")
    with open(name + ".txt", "a") as input_file:
        while new_line != "stop":
            input_file.write(new_line + "\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
