# rer8
def main() -> None:
    name = input("Enter name of the file: ")
    write_text = ""
    while True:
        text_input = input("Enter new line of content: ")
        if text_input == "stop":
            break
        write_text += text_input + "\n"
    print(write_text)
    with open(f"{name}.txt", "a") as file:
        file.write(write_text)


if __name__ == "__main__":
    main()
