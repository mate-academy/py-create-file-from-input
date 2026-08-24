def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    file_name = file_name + ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"File {file_name} created successfully!")


if __name__ == "__main__":
    main()
