def main() -> None:
    file_name = input("Enter name of the file: ").strip()

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    output_path = f"{file_name}.txt"
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f'\nFile "{output_path}" created successfully.')


if __name__ == "__main__":
    main()
