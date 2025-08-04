def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    full_name = f"{file_name}.txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(full_name, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"File '{full_name}' created successfully.")


if __name__ == "__main__":
    main()
