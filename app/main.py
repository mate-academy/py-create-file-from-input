def main() -> None:
    file_name = input("Enter name of the file: ")
    data_file = open(f"{file_name}.txt", "w")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        data_file.write(new_line + "\n")

    data_file.close()


if __name__ == "__main__":
    main()
