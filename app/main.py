def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            file.write(text + "\n")


if __name__ == "__main__":
    main()
