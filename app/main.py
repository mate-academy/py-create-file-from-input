def main() -> None:
    filename_base = input("Enter name of the file: ").strip()
    name = f"{filename_base}.txt"

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(name, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print("File content: ")

    with open(name, "r") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    main()
