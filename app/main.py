def main() -> None:
    filename: str = input("Enter name of the file: ")

    content: str = ""
    line: str = input("Enter new line of content: ")
    while line != "stop":
        content += line + "\n"
        line = input("Enter new line of content: ")

    with open(f"{filename}.txt", "w") as file:
        file.write(content)

    print(f'Name of the file: "{filename}.txt"\nContent file:\n{content}')


if __name__ == "__main__":
    main()
