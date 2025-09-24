def main():
    # Ask for the file name
    file_name = input("Enter name of the file: ") + ".txt"

    lines = []
    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        lines.append(content)

    # Create and write into the file
    with open(file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"\nFile '{file_name}' created successfully!")
    print("File content:")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
