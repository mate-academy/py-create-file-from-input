def main() -> None:
    file_name = input("Enter name of the file: ")
    new_file = open(f"{file_name}.txt", "x")
    new_file.close()
    new_file = open(f"{file_name}.txt", "a")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        new_file.write(new_line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
