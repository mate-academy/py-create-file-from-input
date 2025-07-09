def main():
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        text.append(content)

    with open(f"{file_name}.txt", "w") as file:
        for element in text:
            file.write(element + "\n")


if __name__ == "__main__":
    main()
