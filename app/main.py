def main() -> None:
    file_name = input("Enter name of the file: ").strip() + ".txt"
    file_content = []

    while True:
        new_content = input("Enter new line of content: ").strip()

        if new_content == "stop":
            with open(file_name, "w") as file:
                file.write("\n".join(file_content))
            break

        if new_content:
            file_content.append(new_content)


if __name__ == "__main__":
    main()
