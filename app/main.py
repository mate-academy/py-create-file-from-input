def main():
    file_name = input("Enter name of the file: ").strip()
    if not file_name.lower().endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        entry = input("Enter new line of content: ")
        if entry.strip().lower() == "stop":
            break
        lines.append(entry)

    with open(file_name, "w") as f:
        f.writelines(line + "\n" for line in lines)


if __name__ == "__main__":
    main()
