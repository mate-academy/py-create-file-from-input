def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"
    print("Enter lines to write to the file.")
    print("When you're done, type 'stop' and press Enter.\n")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(file_name, "a") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"File '{file_name}' has been successfully created and saved!")


if __name__ == "__main__":
    main()
