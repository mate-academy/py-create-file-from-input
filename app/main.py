def main() -> None:
    file_name = input("Enter name of the file: ")
    user_file = open(file_name + ".txt", "a")
    line = ""
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            user_file.write(line + "\n")
    user_file.close()


if __name__ == "__main__":
    main()
