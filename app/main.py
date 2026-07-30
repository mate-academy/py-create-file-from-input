def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    info = ""
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        info += content + "\n"
    with open(filename, "w") as f:
        f.write(info)


if __name__ == "__main__":
    main()
