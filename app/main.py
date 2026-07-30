def main() -> None:
    lines = []
    welcome_line = "Enter name of the file: "
    file_name = input(welcome_line)
    file_name = file_name + ".txt"

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        lines.append(new_line)

    file_instance = open(file_name, "w")
    for line in lines:
        suffix = "\n"
        file_instance.write(f"{line}{suffix}")
    file_instance.close()


if __name__ == "__main__":
    main()
