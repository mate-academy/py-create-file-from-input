def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        line = input("Enter new line of content: ")
        while line != "stop":
            file.write(line + "\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
