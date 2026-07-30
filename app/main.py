def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name:
        with open(f"{file_name}.txt", "w") as file_:
            new_line = input("Enter new line of content: ")
            while new_line != "stop":
                file_.write(new_line + "\n")
                new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
