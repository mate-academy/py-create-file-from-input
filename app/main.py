def main() -> None:
    file_name = input("Enter name of the file: ")
    created_file = open(f"{file_name}.txt", "w")
    created_file.close()
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        created_file = open(f"{file_name}.txt", "a")
        created_file.write(new_line + "\n")
    created_file.close()


if __name__ == "__main__":
    main()
