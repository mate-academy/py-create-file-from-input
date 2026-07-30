def main() -> None:
    file_name = input("Enter name of the file: ")
    file_lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file_lines.append(new_line)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(file_lines))


if __name__ == "__main__":
    main()
