def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as file_record:
        content = input("Enter new line of content: ")
        while content.strip() != "stop":
            file_record.write(f"{content}\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
