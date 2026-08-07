def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        co_in = input("Enter new line of content: ")
        if co_in.lower() == "stop":
            break
        content.append(co_in)
    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
