def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w") as f:
        f.write("\n".join(content))

    print(f"File '{file_name}' created successfully.")


if __name__ == "__main__":
    main()
