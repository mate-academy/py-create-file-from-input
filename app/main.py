def main():
    title = input("Enter name of the file: ")
    title += ".txt"
    content_input = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        content_input.append(content)

    with open(title, "w") as file:
        file.write("\n".join(content_input))


if __name__ == "__main__":
    main()
