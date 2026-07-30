def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as file:
        while True:
            next_line = input("Enter new line of content: ")

            if next_line == "stop":
                break

            file.write(next_line + "\n")


if __name__ == "__main__":
    main()
