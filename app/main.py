def main() -> None:
    name = input("Enter name of the file: ")
    all_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break

        all_lines.append(line)

    with open(f"{name}.txt", "a") as record:
        for line in all_lines:
            record.write(line + "\n")



if __name__ == "__main__":
    main()
