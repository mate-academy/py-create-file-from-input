def main():
    file_name = input("Enter name of the file: ").strip()
    full_file_name = f"{file_name}.txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(full_file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"File \"{full_file_name}\" created successfully.")


if __name__ == "__main__":
    main()
