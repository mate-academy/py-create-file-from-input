def main():
    file_name = input("Enter name of the file: ").strip()

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":  # Користувач завершує введення
            break
        lines.append(line)

    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"File '{file_name}' has been created successfully!")


if __name__ == "__main__":
    main()
