def main() -> None:
    name = input("Enter name of the file: ")
    name = name + ".txt"
    lines = []
    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        else:
            lines.append(content)
    with open(name, "w") as n:
        for line in lines:
            n.write(f"{line}\n")


if __name__ == "__main__":
    main()
