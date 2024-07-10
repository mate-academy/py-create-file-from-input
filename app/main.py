def main() -> None:
    name = input("Enter name of the file: ")
    content = []
    while True:
        input_text = input("Enter new line of content: ")
        if input_text != "stop":
            content.append(input_text)
        else:
            break
    with open(name + ".txt", "a") as f:
        if content:
            for element in content:
                f.write(f"{element}\n")


if __name__ == "__main__":
    main()
