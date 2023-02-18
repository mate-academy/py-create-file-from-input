def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as first_file:
        string = ""
        while string != "stop":
            string = input("Enter new line of content: ")
            if string != "stop":
                first_file.write(string)
                first_file.write("\n")


if __name__ == "__main__":
    main()
