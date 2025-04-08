def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    file_content = []

    while True:
        line = input("Enter new line of content: ").strip()
        if line.lower() == "stop":
            break
        file_content.append(line)

    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(file_content))


if __name__ == "__main__":
    main()
