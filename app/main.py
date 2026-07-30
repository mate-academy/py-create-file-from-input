def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        text_for_file = input("Enter new line of content: ")
        while text_for_file != "stop":
            f.write(f"{text_for_file}\n")
            text_for_file = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
