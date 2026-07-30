def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            else:
                file.write(new_line + "\n")


if __name__ == "__main__":
    main()
