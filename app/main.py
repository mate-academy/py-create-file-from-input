def main() -> None:
    file_name: str = input("Enter name of the file: ")
    file_contents: list[str] = []
    while (data := input("Enter new line of content: ")) != "stop":
        file_contents.append(data)
    with open(f"{file_name}.txt", "w") as fobj:
        fobj.write("\n".join(file_contents))


if __name__ == "__main__":
    main()
