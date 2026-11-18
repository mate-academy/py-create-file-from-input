def main():
    file_name = input("Enter name of the file: ")
    messages = []
    while True:
        message = input("Enter new line of content: ")
        if message == "stop":
            break
        messages.append(message)

    with open(file_name + ".txt", "w") as file:
        file.write("\n".join(messages))


if __name__ == "__main__":
    main()