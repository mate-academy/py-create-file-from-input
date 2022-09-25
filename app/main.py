def main():
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as file:
        while 1:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
