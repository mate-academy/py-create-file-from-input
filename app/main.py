def main():
    file_name = input("Enter name of the file: ")
    with open(file_name, "a") as file:
        while True:
            text = input("Enter new line of content:")
            file.write(text + "\n")
            if text == "stop":
                break

if __name__ == "__main__":
    main()
