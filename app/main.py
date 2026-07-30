def main() -> None:
    name = input("Enter name of the file: ").strip()
    if not name:
        print("No file name given")
        return

    if not name.lower().endswith(".txt"):
        name = name + ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    try:
        with open(name, "w") as f:
            for ln in lines:
                f.write(ln)
                f.write("\n")
        print(f"File '{name}' created successfully.")
    except IOError as e:
        print("Error writing file:", e)


if __name__ == "__main__":
    main()
