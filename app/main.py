def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    my_file = open(file_name, "a")
    my_file.close()
    while True:
        line_content = input("Enter new line of content: ")
        if line_content != "stop":
            with open(file_name, "a+") as f:
                f.write(line_content + "\n")
        else:
            break


if __name__ == "__main__":
    main()
