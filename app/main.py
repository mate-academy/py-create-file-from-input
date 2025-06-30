def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file:
        file.write(f'File name: "{file_name}"\n')
        file.write("File content:\n")
        while True:
            new_line = input("Enter new line of content: ")
            if new_line.lower() == "stop":
                break
            file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
