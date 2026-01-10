def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line.strip().lower() == "stop":
                break

            f.write(line + "\n")

    print(f'File "{file_name}" created successfully!')


if __name__ == "__main__":
    main()
