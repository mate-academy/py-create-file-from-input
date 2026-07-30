def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    file_path = f"{file_name}.txt"

    with open(file_path, "w") as file:
        for line in lines:
            file.write(f"{line}\n")

    print(
        f"File '{file_name}.txt' "
        f"successfully created with the following content:"
    )
    for line in lines:
        print(f"# {line}")


if __name__ == "__main__":
    main()
