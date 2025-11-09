def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    file_name_etx = f"{file_name}.txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name_etx, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
