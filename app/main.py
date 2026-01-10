def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "w") as file_to_write:
        content = input("Enter new line of content: ")
        while content != "stop":
            file_to_write.write(content + "\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
