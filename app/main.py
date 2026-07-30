def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    while True:
        with open(file_name, "a") as file:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line.strip() + "\n")


if __name__ == "__main__":
    main()
