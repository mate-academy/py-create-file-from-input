def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        if line.strip():
            lines.append(line)
    with open(file_name, "w") as f:
        if lines:
            f.write("\n".join(lines) + "\n")

    print(f"File saved: {file_name} with {len(lines)} lines.")


if __name__ == "__main__":
    main()
