def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        while True:
            text = input("Enter new line of content: ")
            if text.lower() == "stop":
                break
            f.write(text + "\n")


if __name__ == "__main__":
    main()
