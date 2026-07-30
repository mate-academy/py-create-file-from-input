def main() -> None:
    filename = input("Enter name of the file: ")

    full_filename = filename + ".txt"

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(full_filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"File '{full_filename}' has been created successfully.")


if __name__ == "__main__":
    main()
