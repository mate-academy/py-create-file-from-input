def main() -> None:
    file_name = input("Enter name of the file: ")

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            with open(f"{file_name}.txt", "a") as file:
                file.write("")
            break
        with open(f"{file_name}.txt", "a") as file:
            file.write(f"{str(new_line)}\n")


if __name__ == "__main__":
    main()
