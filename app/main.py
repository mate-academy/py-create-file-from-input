def main() -> None:
    file_basename = input("Enter name of the file: ")
    content = []
    if not file_basename.endswith(".txt"):
        file_basename += ".txt"
    print(file_basename)

    line = input("Enter new line of content: ")
    while line != "stop":
        content.append(line)
        line = input("Enter new line of content: ")

    with open(file_basename, "w") as f:
        for line in content:
            f.write(line)
            f.write("\n")


if __name__ == "__main__":
    main()
