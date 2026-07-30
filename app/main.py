def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as f:
        while True:
            input_line = input("Enter new line of content: ")
            if input_line == "stop":
                return
            f.write(f"{input_line}\n")


if __name__ == "__main__":
    main()
