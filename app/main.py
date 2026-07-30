def main() -> None:
    create_file = input("Enter name of the file: ")
    with open(create_file + ".txt", "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
