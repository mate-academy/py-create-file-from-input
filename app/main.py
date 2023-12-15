def main() -> None:
    name = input("Enter name of the file: ")
    context = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            context.append(line)
    file_path = name + ".txt"
    with open(file_path, "w") as file:
        file.write("\n".join(context))


if __name__ == "__main__":
    main()
