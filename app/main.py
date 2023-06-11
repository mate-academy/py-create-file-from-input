def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "w") as f:
        while True:
            content = input("Enter new line of content: ") + "\n"
            if content == "stop\n":
                break
            f.write(content)


if __name__ == "__main__":
    main()
