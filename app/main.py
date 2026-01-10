def main() -> bool:
    name = input("Enter name of the file: ")
    line = "  "
    content = []
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            content.append(line)

    with open(f"{name}.txt", "w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
