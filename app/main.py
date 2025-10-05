def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    while True:
        next_line = input("Enter new line of content: ")

        if next_line == "stop":
            with open(f"{file_name}.txt", "w") as new_file:
                new_file.write(content)
                break
        else:
            content += f"{next_line}\n"


if __name__ == "__main__":
    main()
