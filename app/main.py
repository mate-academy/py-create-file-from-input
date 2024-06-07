def main() -> None:
    file_name = str(input("Enter name of the file: "))

    while True:
        with open(f"{file_name}.txt", "a") as f:
            row = input("Enter new line of content: ")
            if row == "stop":
                break
            if row:
                f.write(row + "\n")
            else:
                f.write()


if __name__ == "__main__":
    main()
