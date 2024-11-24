def main() -> None:
    file_name = input("Enter name of the file: ")
    next_input = ""
    with open(f"{file_name}.txt", "a") as f:
        while next_input != "stop":
            next_input = input("Enter new line of content: ")
            if next_input == "stop":
                break
            f.write(f"{next_input}\n")


if __name__ == "__main__":
    main()
