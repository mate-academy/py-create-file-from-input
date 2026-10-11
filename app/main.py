def main() -> None:
    name_file = input("Enter name of the file: ")
    with open(f"{name_file}.txt", "w") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            file.write(new_line + "\n")


if __name__ == "__main__":
    main()
