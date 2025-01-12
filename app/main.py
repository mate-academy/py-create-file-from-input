def main() -> None:
    file_name = input("Enter name of the file: ")

    new_file = open(f"{file_name}.txt", "a")

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        new_file.write(line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
