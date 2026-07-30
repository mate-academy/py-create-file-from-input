def main() -> None:
    filename = input("Enter name of the file: ")
    value = []
    while True:
        content = input("Enter new line of content: ")
        if "stop" in content:
            break
        value.append(content)

    with open(f"{filename}.txt", "a") as f:
        for line in value:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
