def main() -> None:
    result = []
    name = input("Enter name of the file: ")
    if not name.endswith(".txt"):
        name = name + ".txt"
    while True:
        listen = input("Enter new line of content: ")
        if listen.lower() == "stop":
            break
        result.append(listen)

    with open(name, "w", encoding="utf-8") as f:
        for line in result:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
