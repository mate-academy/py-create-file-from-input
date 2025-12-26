def main() -> None:

    file_name = input("Enter name of the file: ")

    file_name = f"{file_name}.txt"

    content = []

    print("Enter new line of content (type 'stop' to finish):")

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

    print(f"File '{file_name}' created "
          f"successfully with the following content: ")
    print("\n".join(content))


if __name__ == "__main__":
    main()
