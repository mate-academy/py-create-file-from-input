def main() -> None:
    name = input("Enter name of the file: ")
    if not name.endswith(".txt"):
        fullname = name + ".txt"
    else:
        fullname = name
    lines = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        lines.append(content)
    with open(fullname, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
