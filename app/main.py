def main() -> None:
    file_name = input("Enter name of the file: ")
    while True:
        with open(f"{file_name}.txt", "a") as file:
            new_line = input("Enter new line of content: ")

            if new_line == "stop":
                break
            file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
