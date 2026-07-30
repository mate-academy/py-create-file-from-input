def main() -> None:
    file_name = input("Enter name of the file: ")
    file_with_extension = file_name + ".txt"
    new_file = open(file_with_extension, "w")
    while True:
        file_content = input("Enter new line of content: ")
        if file_content == "stop":
            break
        with open(file_with_extension, "a") as existing_file:
            existing_file.write(file_content + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
