def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    our_string = input("Enter new line of content: ") + "\n"
    with open(file_name, "a") as f:
        while our_string != "stop\n":
            f.write(our_string)
            our_string = input("Enter new line of content: ") + "\n"


if __name__ == "__main__":
    main()
