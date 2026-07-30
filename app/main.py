def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file:
        your_text = None
        while your_text != "stop":
            your_text = input("Enter new line of content: ")
            if your_text != "stop":
                file.write(your_text + "\n")


if __name__ == "__main__":
    main()
