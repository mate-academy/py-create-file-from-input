def main() -> None:
    result = []
    new_name = input("Enter name of the file: ")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        result.append(line)
    with open(f"{new_name}.txt", "w") as file:
        for line in result:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
