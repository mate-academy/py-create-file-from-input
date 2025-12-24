def main() -> None:
    name = input("Enter name of the file: ")
    data = []

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        data.append(line)

    with open(f"{name}.txt", "w") as file:
        file.write("\n".join(data))


if __name__ == "__main__":
    main()
