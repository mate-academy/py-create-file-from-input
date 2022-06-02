def main():
    name = input("Enter name of the file: ")
    file = open(f"{name}.txt", "a")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file.write(f"{content}\n")


if __name__ == "__main__":
    main()
