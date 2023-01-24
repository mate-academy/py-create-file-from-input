def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as file:
        while True:
            file_line = input("Enter new line of content: ")
            if file_line == "stop":
                break
            file.writelines(file_line + "\n")


if __name__ == "__main__":
    main()
