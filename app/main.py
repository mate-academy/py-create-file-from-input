def main() -> None:
    name_file = input("Enter name of the file: ")
    name_file = f"{name_file}.txt"
    with open(name_file, "w") as file:
        text = ""
        while text != "stop":
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            file.write(f"{text}\n")


if __name__ == "__main__":
    main()
