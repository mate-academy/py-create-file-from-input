def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        input_message = input("Enter new line of content: ")
        if input_message != "stop":
            content.append(input_message)
        else:
            break

    with open(f"{name}", "a") as f:
        if content:
            for message in content:
                f.write(message + "\n")


if __name__ == "__main__":
    main()
