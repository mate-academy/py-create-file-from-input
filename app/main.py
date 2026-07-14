def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as result_file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop".lower():
                break
            else:
                result_file.write(text + "\n")


if __name__ == "__main__":
    main()
