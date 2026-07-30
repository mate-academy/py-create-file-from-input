def main() -> None:
    text = ""

    file_name = input("Enter name of the file: ")
    if file_name:
        with open(file_name + ".txt", "w") as f:
            while text != "stop":
                text = input("Enter new line of content: ")
                if text != "stop":
                    f.write(text + "\n")


if __name__ == "__main__":
    main()
