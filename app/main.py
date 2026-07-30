def main() -> None:
    file_name = input("Enter name of the file: ")
    line_w = []
    while True:
        content = input("Enter new line of content: ")
        if "stop" in content:
            break
        line_w.append(content)
    with open(f"{file_name}.txt", "a") as f:
        for line in line_w:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
