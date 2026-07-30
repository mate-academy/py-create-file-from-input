def main() -> None:
    file_name = input("Enter name of the file: ").strip()

    if not file_name:
        raise ValueError

    with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
        while True:
            text_input = input("Enter new line of content: ")

            if text_input == "stop":
                break

            f.write(text_input + "\n")


if __name__ == "__main__":
    main()
