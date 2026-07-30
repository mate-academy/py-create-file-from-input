def main() -> None:
    filename = input("Enter name of the file: ")
    current_lines = []
    while True:
        data = input("Enter new line of content: ")
        if data.lower() == "stop":
            break
        current_lines.append(data)

    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(current_lines))


if __name__ == "__main__":
    main()
