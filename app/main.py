def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        else:
            lines.append(f"{text}\n")

    with open(f"{file_name}.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
