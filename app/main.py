def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    line = ""
    with open(file_name, "w") as file:
        while line != "stop\n":
            file.write(line)
            line = input("Enter new line of content: ") + "\n"


if __name__ == "__main__":
    main()
