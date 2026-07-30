def main() -> None:
    filename_input = input("Enter name of the file: ")
    filename = filename_input + ".txt"
    with open(filename, "a") as file:
        while True:
            line_input = input("Enter new line of content: ")
            if line_input != "stop":
                file.write(line_input + "\n")
            elif line_input == "stop":
                break
    print(f"File name: '{filename}'")
    with open(filename, "r") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    main()
