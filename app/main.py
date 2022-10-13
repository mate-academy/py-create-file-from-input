def main() -> str:
    file_name = input("Enter name of the file: ")
    new_file_line = ""
    with open(f"{file_name}.txt", "a") as f:
        while new_file_line != "stop":
            new_file_line = input("Enter new line of content: ")
            if new_file_line == "stop":
                break
            f.write(f"{new_file_line}\n")


if __name__ == "__main__":
    main()
