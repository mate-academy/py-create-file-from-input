def main() -> None:

    name = input("Enter name of the file: ")

    all_text = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        all_text.append(line)

    with open(f"{name}.txt", "a") as report:
        for line in all_text:
            report.write(line + "\n")


if __name__ == "__main__":
    main()
