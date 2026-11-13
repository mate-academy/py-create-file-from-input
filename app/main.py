def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    output_file = open(f"{file_name}.txt", "w")
    for line in lines:
        output_file.write(f"{line}\n")
    output_file.close()


if __name__ == "__main__":
    main()
