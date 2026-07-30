def main() -> None:
    file_name = ""
    while not file_name:
        file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "w") as f:
        new_line = input("Enter new line of content: ")
        while not new_line == "stop":
            f.write(new_line + "\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
