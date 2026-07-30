def main() -> None:
    name_of_file = input("Enter name of the file: ")
    content = []
    while True:
        second_str = input("Enter new line of content: ")
        if str(second_str) == "stop":
            break
        content.append(second_str)
    with open(f"{name_of_file}.txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
