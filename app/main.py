def main() -> str:
    file_name = input("Enter name of the file: ")
    container = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        container.append(line)

    with open(f"{file_name}.txt", "w") as file:
        for line in container:
            file.write(f"{line}\n")
        print(f"File '{file_name}.txt'")


if __name__ == "__main__":
    main()
