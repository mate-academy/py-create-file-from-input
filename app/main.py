def main() -> None:
    """Funkcja wprowadza teskt do utowrzonego pliku"""

    name_file = input("Enter name of the file: ")
    name_file_txt = f"{name_file}.txt"

    with open(f"{name_file_txt}", "w", encoding="utf-8") as file:
        while True:
            massage = input("Enter new line of content: ")
            if massage == "stop":
                break
            file.write(f"{massage}\n")


if __name__ == "__main__":
    main()
