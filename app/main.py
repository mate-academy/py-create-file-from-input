def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    with open(file_name, "w") as file1:
        while True:
            file_line = input("Enter new line of content: ")

            if file_line == "stop":
                break

            file1.write(file_line + "\n")


if __name__ == "__main__":
    main()
