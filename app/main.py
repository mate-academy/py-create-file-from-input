def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name and not file_name.endswith(".txt"):
        file_name += ".txt"
    if file_name:
        with open(file_name, "a") as f:
            while True:
                new_line = input("Enter new line of content: ")
                if new_line == "stop":
                    break
                f.write(new_line + "\n")


if __name__ == "__main__":
    main()
