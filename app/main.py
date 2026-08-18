def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
