def main() -> None:
    lines = []
    file_name = input("Enter name of the file: ") + ".txt"
    while True:
        user_input = input("Enter new line of content: ")
        if user_input.lower() == "stop":
            break
        else:
            lines.append(user_input)

    with open(file_name, "w") as f:
        if lines:
            f.write("\n".join(lines) + "\n")
        else:
            f.write("")


if __name__ == "__main__":
    main()
