def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(name_of_file + ".txt", "w") as f:
        file_content = input("Enter new line of content: ")
        while file_content != "stop":
            f.write(file_content + "\n")
            file_content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
