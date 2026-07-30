def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_content.append(line)

    file_path = file_name + ".txt"
    with open(file_path, "w") as file:
        file.write("\n".join(file_content))

    print(f"\nFile name: {file_name}.txt")
    print("File content:")
    print("\n".join(file_content))


if __name__ == "__main__":
    main()
