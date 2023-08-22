def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    work_file = open(file_name, "a")

    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        work_file.write(text + "\n")

    work_file.close()


if __name__ == "__main__":
    main()
