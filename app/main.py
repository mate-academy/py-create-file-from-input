def main():
    filename = input("Enter name of the file: ") + ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"File '{filename}' created with your content.")


if __name__ == "__main__":
    main()
