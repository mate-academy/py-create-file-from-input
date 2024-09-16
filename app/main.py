def main():
    file_name = input("Enter name of the file: ")
    open(f"{file_name}.txt", "w")

    while True:
        content = input("Enter new line of content: ")

        if content.lower() == "stop":
            return
        else:
            with open(f"{file_name}.txt", "a") as f:
                f.write(content + "\n")


if __name__ == "__main__":
    main()
