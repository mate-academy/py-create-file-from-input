def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as file:
        # file.write(f'File name: "{file_name}.txt"\n')
        # file.write("File content:\n")
        while True:
            line_input = input("Enter new line of content: ")
            if line_input == "stop":
                break
            file.write(line_input)
            file.write("\n")


if __name__ == "__main__":
    main()
