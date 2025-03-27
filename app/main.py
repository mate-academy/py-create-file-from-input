def main() -> None:
    file_name = input("Enter name of the file: ")

    if "." not in file_name:
        file_name += ".txt"

    with open(file_name, "w") as f:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            f.write(new_line + "\n")


if __name__ == "__main__":
    main()
