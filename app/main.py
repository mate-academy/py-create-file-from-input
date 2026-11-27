def main() -> None:
    name = input("Enter name of the file: ")
    all_new_line = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        all_new_line.append(new_line)
    name = f"{name}.txt"
    with open(name, "w") as f:
        text = "".join(f"{line}\n" for line in all_new_line)
        f.write(text)


if __name__ == "__main__":
    main()
