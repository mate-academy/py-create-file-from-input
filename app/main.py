def main() -> None:
    file_name = input("Enter name of the file: ")
    content_to_write = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        content_to_write.append(content)

    content_to_write = "\n".join(content_to_write).strip()
    with open(f"{file_name}.txt", "w") as f:
        f.write(content_to_write)


if __name__ == "__main__":
    main()
