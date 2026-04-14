def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    result = []

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        result.append(content)

    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(result))


if __name__ == "__main__":
    main()
