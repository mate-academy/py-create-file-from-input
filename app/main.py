def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "w", encoding="utf-8") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
