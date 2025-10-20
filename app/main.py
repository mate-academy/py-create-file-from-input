def main() -> None:
    file_name = str(input("Enter name of the file: "))
    file_name += ".txt"
    with open(file_name, "a") as file:
        while True:
            new_line = str(input("Enter new line of content: "))
            if new_line == "stop":
                break
            file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
