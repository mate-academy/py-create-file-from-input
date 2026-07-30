def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        while True:
            line_input = input("Enter new line of content: ")
            if line_input.lower() == "stop":
                break
            file.write(f"{line_input}\n")


if __name__ == "__main__":
    main()
