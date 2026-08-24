def main() -> None:
    file_name = input("Enter name of the file: ")
    content_line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as file:
        while content_line != "stop":
            file.write(f"{content_line}\n")
            content_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
