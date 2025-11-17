def main():
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        lines.append(content)

    with open(f"{file_name}.txt", "a") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
