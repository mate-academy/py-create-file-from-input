def main():
    filename = input("Enter name of the file: ")
    content = ""

    while True:
        temp = input("Enter new line of content: ")
        if temp.lower() == "stop":
            break
        content += temp + "\n"

    with open(f"{filename}.txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
