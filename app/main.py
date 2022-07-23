def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        while True:
            text = input("Enter new line of content: ")

            if text == "stop":
                break

            print(text, file=f)


if __name__ == "__main__":
    main()
