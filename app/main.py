def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    output_name = f"{file_name}.txt"
    with open(output_name, "w") as f:
        f.write("\n".join(lines))
    print(f'Created "{output_name}" with {len(lines)} line(s).')


if __name__ == "__main__":
    main()
