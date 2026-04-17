def main() -> None:
    trigger = True
    text = []
    name = input("Enter name of the file: ") + ".txt"
    while trigger:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        else:
            text.append(new_line + "\n")
    with open(name, "w") as f:
        f.writelines(text)


if __name__ == "__main__":
    main()
