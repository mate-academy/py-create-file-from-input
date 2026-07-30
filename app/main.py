def main() -> None:
    file_name = input("Enter name of the file: ")
    work_file = open(file_name + ".txt", "w")
    while True:
        user_text = input("Enter new line of content: ")
        if user_text == "stop":
            break
        work_file.write(user_text + "\n")
    work_file.close()


if __name__ == "__main__":
    main()
