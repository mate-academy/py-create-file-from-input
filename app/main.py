def main() -> None:
    filename = input("Enter name of the file: ")
    text = None
    content = []

    while text != "stop":
        text = input("Enter new line of content: ")
        if text != "stop":
            content.append(text)

    with open(f"{filename}.txt", "w") as f:
        print("File content:")
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
