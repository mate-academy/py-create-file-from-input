def main() -> None:
    enter_file_name = input("Enter name of the file: ")
    file_name = enter_file_name + ".txt"

    with open(file_name, "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
