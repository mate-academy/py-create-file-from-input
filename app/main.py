def main() -> None:
    name = input("Enter name of the file: ")
    name = f"{name}.txt"
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(f"{line}\n")

    with open(name, "w") as e:
        e.writelines(content)


if __name__ == "__main__":
    main()
