def main() -> None:
    text = ""
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"

    with open(f"{file_name}", "a") as f:
        while text != "stop":
            text = input("Enter new line of content: ")
            if text != "stop":
                f.write(text + "\n")


if __name__ == "__main__":
    main()
