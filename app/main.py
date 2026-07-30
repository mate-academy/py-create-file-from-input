def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            row = input("Enter new line of content: ")
            if row == "stop":
                break
            file.write(row + "\n")


if __name__ == "__main__":
    main()
