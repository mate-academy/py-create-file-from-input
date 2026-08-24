def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    with open(file_name, "a") as work_file:
        while True:
            text = input("Enter new line of content: ")
            if text != "stop":
                work_file.write(text + "\n")
            else:
                break


if __name__ == "__main__":
    main()
