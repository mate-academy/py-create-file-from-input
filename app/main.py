def main():
    name = input("Enter name of the file: ")
    content = input("Enter new line of content: ")
    with open(f"{name}.txt", "a") as f:
        while content != "stop":
            f.write(f"{content}\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
