def main() -> None:
    filename = input("Enter name of the file: ")
    user_lines = []

    while True:
        user_text = input("Enter new line of content: ")

        if user_text == "stop":
            break

        user_lines.append(user_text)

    with open(f"{filename}.txt", "w") as f:
        for line in user_lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
