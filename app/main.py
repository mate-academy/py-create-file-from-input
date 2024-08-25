def main() -> None:
    file_name = input("Enter name of the file: ")

    file = open(f"{file_name}.txt", "x")
    file.close()

    new_line = input("Enter new line of content: ")
    while new_line != "stop":

        with open(f"{file_name}.txt", "a") as new_file:
            new_file.write(f"{new_line}\n")
        new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
