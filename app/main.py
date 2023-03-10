def main() -> None:
    file_name = str(input("Enter name of the file: "))
    file_content = input("Enter new line of content: ")
    with open((file_name + ".txt"), "a") as file:
        while file_content != "stop":
            file.write(str(file_content) + "\n")
            file_content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
