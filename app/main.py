def main() -> None:
    file_name = input("Enter name of the file: ")
    storage = []
    input_text = ""
    while input_text != "stop":
        storage.append(input_text)
        input_text = input("Enter new line of content: ")

    with open(file_name + ".txt", "a") as file:
        del storage[0]
        file.write("\n".join(storage))


if __name__ == "__main__":
    main()
