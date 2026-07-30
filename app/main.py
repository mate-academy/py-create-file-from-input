def main() -> object:
    file_name = input("Enter name of the file: ")
    texts = ""
    while True:
        string = input("Enter new line of content: ")
        if string != "stop":
            texts += string + "\n"
        elif string == "stop":
            break
    with open(f"{file_name}.txt", "w") as f:
        f.write(texts)

    with open(f"{file_name}.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
