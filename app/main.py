def main() -> None:
    filename = input("Enter name of the file: ").strip()
    full_name = f"{filename}.txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(full_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f'File "{full_name}" has been created.')


if __name__ == "__main__":
    main()
