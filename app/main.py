def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    line = input("Enter new line of content: ")
    while line != "stop":
        content.append(line)
        line = input("Enter new line of content: ")
    file_name = file_name.strip() + ".txt"
    with open(file_name, "w") as f:
        f.write("\n".join(content))
    print(f"File name: {file_name}")
    print("File content:")
    for line in content:
        print(line)


if __name__ == "__main__":
    main()
