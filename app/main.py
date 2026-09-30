def main() -> None:
    file_name = input("Enter name of the file: ")
    arr = []

    while True:
        file_content = input("Enter new line of content: ")

        if file_content.lower() == "stop":
            break
        arr.append(file_content)

    with open(file_name + ".txt", "a") as file:
        for item in arr:
            file.write(item + "\n")


if __name__ == "__main__":
    main()
