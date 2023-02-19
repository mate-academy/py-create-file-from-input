def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as record:
        while True:
            lines = input("Enter new line of content: ")
            if lines == "stop":
                break
            record.write(f"{lines}\n")


if __name__ == "__main__":
    main()
