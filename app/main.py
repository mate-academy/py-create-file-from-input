def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as file:
        while True:
            file_line = input("Enter new line of content: ")
            if file_line == "stop":
                break
            file_line += "\n"
            file.write(file_line)


if __name__ == "__main__":
    main()
