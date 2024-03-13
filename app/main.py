def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        line = input("Enter new line of content (enter 'stop' to finish): ")
        if line.lower() == "stop":
            break
        file_content.append(line)

    file_extension = file_name + ".txt"

    with open(file_extension, "w") as f:
        for line in file_content:
            f.write(line + "\n")

    print(f"File name: \'{file_extension}\'")
    print("File content:")
    for line in file_content:
        print(f"# {line}")


if __name__ == "__main__":
    main()
