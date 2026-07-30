def main() -> None:
    name_of_file = input("Enter name of the file: ")
    if not name_of_file.endswith(".txt"):
        name_of_file += ".txt"

    file_to_write = open(name_of_file, "w")

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        file_to_write.write(f"{user_input}\n")

    file_to_write.close()


if __name__ == "__main__":
    main()
