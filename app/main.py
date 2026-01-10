def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    with open(file_name + ".txt", "w") as file:
        while True:
            message = input("Enter new line of content: ")
            if message == "stop":
                break
            text.append(message)
        file.write("\n".join(text))


if __name__ == "__main__":
    main()
