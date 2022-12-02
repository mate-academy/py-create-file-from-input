def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            content = input("Enter new line of content: ") + "\n"
            if content == "stop\n":
                break
            file.write(content)


if __name__ == "__main__":
    main()
