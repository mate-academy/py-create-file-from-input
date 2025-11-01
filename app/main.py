def main() -> None:

    name = input("Enter name of the file: ").strip()
    if not name.lower().endswith(".txt"):
        name += ".txt"

    with open(name, "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line.strip().lower() == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
