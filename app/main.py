def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        line_content = input("Enter new line of content: ")
        while line_content != "stop":
            file.write(f"{line_content}\n")
            line_content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
