def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as text:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            text.write(new_line + "\n")


if __name__ == "__main__":
    main()
