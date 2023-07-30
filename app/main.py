
def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    with open(file_name, "a") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line.lower() == "stop":
                break
            file.write(new_line + "\n")


if __name__ == "__main__":
    main()
