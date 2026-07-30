def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as f:
        pass

    content = []
    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        content.append(text)

    if content:
        with open(file_name, "w") as f:
            for line in content[:-1]:
                f.write(line + "\n")
            f.write(content[-1])

    else:
        print("Nothing to write to the file.")


if __name__ == "__main__":
    main()
