def main():
    file_name = (input("Enter name of the file: ") + ".txt")
    print(file_name)

    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        with open(file_name, "a") as file:
            file.write(f"{text}\n")


if __name__ == "__main__":
    main()
