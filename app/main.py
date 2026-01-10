def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        f.write("")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        with open(f"{file_name}.txt", "a") as f:
            f.write(f"{text}\n")


if __name__ == "__main__":
    main()
