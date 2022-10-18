def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as name:
        string = ""
        while string != "stop":
            string = input("Enter new line of content: ")
            if string != "stop":
                name.write(string + "\n")
            else:
                break


if __name__ == "__main__":
    main()
