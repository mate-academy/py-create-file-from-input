def main():
    file_name = input("Enter name of the file: ").strip()

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
