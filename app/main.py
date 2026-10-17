def main() -> None:
    result = []
    name = input("Enter name of the file: ")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        result.append(new_line)
    with open(f"{name}.txt", "w") as file:
        file.write("\n".join(result))


if __name__ == "__main__":
    main()
