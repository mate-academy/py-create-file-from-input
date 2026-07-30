def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    content = ""
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content += (line + "\n")

    with open(file_name, "a") as f:
        f.write(f"{content}")


if __name__ == "__main__":
    main()
