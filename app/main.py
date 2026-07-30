def main() -> None:
    name_file = input("Enter name of the file: ")
    new_file = f"{name_file}.txt"
    with open(new_file, "w") as f:
        while True:
            file_str = input("Enter new line of content: ")
            if file_str.lower() == "stop":
                break
            f.write(file_str + "\n")


if __name__ == "__main__":
    main()
