def main() -> None:
    filename = input("Enter name of the file: ")

    lines: list[str] = []
    try:
        while True:
            content: str = input("Enter new line of content: ")
            if content == "stop":
                break

            if not content:
                continue

            lines.append(content + "\n")
    except KeyboardInterrupt:
        pass

    with open(f"{filename}.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
