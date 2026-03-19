def main() -> None:
    name = input("Enter name of the file: ")
    lines = []
    while True:
        stop = input("Enter new line of content: ")
        if stop == "stop":
            break
        lines.append(stop)
    if not name.endswith(".txt"):
        name = name + ".txt"
        with open(name, "w") as f:
            f.write("\n".join(lines))


if __name__ == "__main__":
    main()
