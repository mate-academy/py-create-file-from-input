def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "w") as file:
        while True:
            record_data = input("Enter new line of content: ")
            if record_data == "stop":
                break
            else:
                file.write(record_data + "\n")


if __name__ == "__main__":
    main()
