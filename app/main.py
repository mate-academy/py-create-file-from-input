def main() -> None:
    name = input("Enter name of the file: ")
    if not name.endswith(".txt"):
        name += ".txt"

    with open(name, "a") as f:
        pass

    while True:
        text = input("Enter new line of content: ")

        if text == "stop":
            break

        with open(name, "a") as f:
            f.write(f"{text}\n")


if __name__ == "__main__":
    main()
