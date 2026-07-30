def main() -> None:
    file_name: str = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, "a") as file:
        while True:
            next_line = input("Enter new line of content: ")
            if next_line != "stop":
                file.write(next_line + "\n")
            else:
                break


if __name__ == "__main__":
    main()
