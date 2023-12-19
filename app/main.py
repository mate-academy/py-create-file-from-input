def main() -> None:
    name = input("Enter name of the file: ")

    content = []

    while True:
        new_line = input(
            "Enter new line of content: "
        )

        if new_line == "stop":
            break
        content.append(new_line)

    with open(f"{name}.txt", "a") as new_file:
        new_file.write("\n".join(content))


if __name__ == "__main__":
    main()
