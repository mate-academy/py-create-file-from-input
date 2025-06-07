def main() -> None:
    append_list = []
    name = input("Enter name of the file:")
    while True:
        content = input("Enter new line of content:")
        if content.lower() == "stop":
            break
        append_list.append(content)
    with open(f"{name}.txt", "a") as f:
        for i in append_list:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
