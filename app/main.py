def main() -> None:
    info = input("Enter name of the file: ")
    word = ""
    while True:
        input_content = input("Enter new line of content: ")
        if input_content == "stop":
            break
        else:
            word += f"{input_content}\n"

    with open(f"{info}.txt", "a") as f:
        f.write(word)


if __name__ == "__main__":
    main()
