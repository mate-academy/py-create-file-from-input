def main() -> None:
    name_of_the_file = input("Enter name of the file: ")
    with open(name_of_the_file + ".txt", "a") as user_file:
        content_of_the_file = input("Enter new line of content: ")
        while content_of_the_file != "stop":
            user_file.write(str(content_of_the_file + "\n"))
            content_of_the_file = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
