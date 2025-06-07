def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    input_array = []

    while True:
        new_line = input("Enter new line of content: ")

        if new_line == "stop":
            break

        input_array.append(new_line)

    with open(f"{file_name}.txt", "w") as f:
        for line in input_array:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
