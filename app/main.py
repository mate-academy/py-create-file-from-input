def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        input_data = input("Enter new line of content: ")
        if input_data == "stop":
            break
        else:
            lines.append(input_data)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
