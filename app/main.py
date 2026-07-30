def create_file(name: str, user_text: list) -> None:
    with open(f"{name}.txt", "w") as f:
        for word in user_text:
            if word != "stop\n":
                f.write(f"{word}")
            else:
                break


def main() -> None:
    name = input("Enter name of the file: ")
    add_text = True
    user_text = []
    while add_text != "stop":
        add_text = input("Enter new line of content: ")
        user_text.append(add_text + "\n")
    create_file(name, user_text)


if __name__ == "__main__":
    main()
