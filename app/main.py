def main() -> None:
    filename = input("Enter name of the file: ")
    if filename[-4:] != ".txt":
        filename += ".txt"
    lines = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        else:
            lines.append(content)
    with open(filename, "w") as f:
        f.write("\n".join(lines))
        f.close()


if __name__ == "__main__":
    main()
