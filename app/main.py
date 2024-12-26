def main() -> None:
    file_name = input("Enter name of th file name:")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    content = []
    line = input("Enter new line of content: ")
    while True:
        if line.lower() == "stop":
            break
        content.append(line)
    with open(file_name, "w") as file:
        file.write("\n".join(content))

    file.close()


if __name__ == "__main__":
    main()
