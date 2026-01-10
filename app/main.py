def main() -> None:
    name_file = input("Enter name of the file: ")
    flag_write = True
    with open(name_file + ".txt", "w") as f:
        while flag_write:
            text_input = input("Enter new line of content: ")
            if text_input == "stop":
                break
            f.write(text_input + "\n")


if __name__ == "__main__":
    main()
