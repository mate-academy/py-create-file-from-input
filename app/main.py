def main() -> None:
    file_name = input("Enter name of the file: ")
    file_obj = open(file_name + ".txt", "a")

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file_obj.write(new_line + "\n")


if __name__ == "__main__":
    main()
