def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_line = ""
    with open(file_name, "a") as f:
        while file_line != "stop":
            file_line = input("Enter new line of content: ")
            if file_line == "stop":
                break
            else:
                f.write(f"{file_line}\n")


if __name__ == "__main__":
    main()
