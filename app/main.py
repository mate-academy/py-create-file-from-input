def main():
    filename = input("Enter name of the file: ").strip()
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(f"{filename}.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
