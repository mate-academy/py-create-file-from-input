
def main():
    name = input("Enter name of the file: ")
    content = []

    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        content.append(next_line)

    with open(f"{name}.txt", "a") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
