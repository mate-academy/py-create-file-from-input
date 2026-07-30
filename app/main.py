def main() -> None:
    filename = input("Enter name of the file: ")

    content = []

    while True:
        temp = input("Enter new line of content: ")

        if temp == "stop":
            break

        content.append(temp)

    with open(f"{filename}.txt", "w") as file:
        for line in content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
