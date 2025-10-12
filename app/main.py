def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "w") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line != "stop":
                file.write(f"{new_line}\n")
            else:
                break


if __name__ == "__main__":
    main()
