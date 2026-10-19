def main() -> None:
    file_name_input = input("Enter name of the file: ")
    file_name = f"{file_name_input}.txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    # Remove o caractere de nova linha da última linha inserida, se houver
    if lines:
        lines[-1] = lines[-1].rstrip("\n")

    with open(file_name, mode="w", encoding="utf-8") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main()
