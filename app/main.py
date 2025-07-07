def main() -> None:
    file_name = input("Enter name of the file: ")
    user_file = open(f"{file_name}.txt", "a")
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        else:
            user_file.write(f"{next_line}\n")
    user_file.close()


if __name__ == "__main__":
    main()
