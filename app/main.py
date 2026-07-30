def main() -> None:
    file_name = input("Enter name of the file: ")
    all_text = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        all_text.append(line)
    with open(f"{file_name}.txt", "w") as f:
        for line in all_text:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
