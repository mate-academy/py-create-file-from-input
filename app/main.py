def main() -> bool:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a+") as first_file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                return False
            else:
                first_file.write(content + "\n")


if __name__ == "__main__":
    main()
