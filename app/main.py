def main() -> None:
    file_name = input("Enter name of the file: ")
    next_line = None
    with open(f"{file_name}.txt", "w") as file:
        # file.write(f'File name: "{file_name}.txt"\n')
        while next_line != "stop\n":
            if next_line:
                file.write(next_line)
            next_line = input("Enter new line of content: ") + "\n"


if __name__ == "__main__":
    main()
