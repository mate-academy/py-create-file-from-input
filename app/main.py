def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        line_value = ""
        while line_value != "stop":
            line_value = input("Enter new line of content: ")
            if line_value == "stop":
                break
            file.write(line_value + "\n")


if __name__ == "__main__":
    main()
