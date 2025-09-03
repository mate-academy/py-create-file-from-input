def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    full_content = ""

    while content == "stop":
        full_content += f"{content}\n"
        content = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as f:
        f.write(full_content)


if __name__ == "__main__":
    main()
