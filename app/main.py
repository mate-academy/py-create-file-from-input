def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        while True:
            line_input = input("Enter new line of content: ")
            if line_input == "stop":
                break
            f.write(f"{line_input}\n")


if __name__ == "__main__":
    main()
